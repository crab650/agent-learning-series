from __future__ import annotations

import time
from collections.abc import Callable
from typing import Any

from schemas import PlanTask, StepResult
from tools import compare_inventory, get_mes_finished_goods_inventory, get_raw_material_inventory


Tool = Callable[..., dict[str, Any]]

TOOL_REGISTRY: dict[str, Tool] = {
    "get_mes_finished_goods_inventory": get_mes_finished_goods_inventory,
    "get_raw_material_inventory": get_raw_material_inventory,
    "compare_inventory": compare_inventory,
}


class ToolExecutor:
    def __init__(self, tool_registry: dict[str, Tool] | None = None):
        self.tool_registry = tool_registry or TOOL_REGISTRY

    def run(self, tasks: list[PlanTask]) -> dict[str, Any]:
        ordered = sorted(tasks, key=lambda t: t.step)
        step_results: dict[int, StepResult] = {}
        step_outputs: dict[int, dict[str, Any]] = {}

        for task in ordered:
            unmet = [s for s in task.depends_on if s not in step_results]
            failed_deps = [
                s for s in task.depends_on if s in step_results and step_results[s].status != "success"
            ]

            if unmet:
                step_results[task.step] = StepResult(
                    step=task.step,
                    action=task.action,
                    status="skipped",
                    skipped_reason=f"Unmet dependencies: {unmet}",
                )
                continue

            if failed_deps:
                step_results[task.step] = StepResult(
                    step=task.step,
                    action=task.action,
                    status="skipped",
                    skipped_reason=f"Failed dependencies: {failed_deps}",
                )
                continue

            tool = self.tool_registry.get(task.action)
            if not tool:
                step_results[task.step] = StepResult(
                    step=task.step,
                    action=task.action,
                    status="failed",
                    error=f"Unknown action: {task.action}",
                )
                continue

            started = time.perf_counter()
            try:
                if task.action == "compare_inventory":
                    output = tool(step_outputs)
                else:
                    output = tool(**task.input)
                elapsed_ms = int((time.perf_counter() - started) * 1000)
                output = {**output, "_meta": {"latency_ms": elapsed_ms}}
                step_outputs[task.step] = output
                step_results[task.step] = StepResult(
                    step=task.step,
                    action=task.action,
                    status="success",
                    output=output,
                )
            except Exception as exc:  # noqa: BLE001
                step_results[task.step] = StepResult(
                    step=task.step,
                    action=task.action,
                    status="failed",
                    error=str(exc),
                )

        overall = self._overall_status(step_results)
        return {
            "step_results": {k: vars(v) for k, v in step_results.items()},
            "final_status": overall,
        }

    @staticmethod
    def _overall_status(step_results: dict[int, StepResult]) -> str:
        statuses = {result.status for result in step_results.values()}
        if statuses == {"success"}:
            return "success"
        if "success" in statuses:
            return "partial_success"
        if "failed" in statuses:
            return "failed"
        return "skipped"
