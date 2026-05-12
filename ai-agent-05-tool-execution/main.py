from __future__ import annotations

import json
from pathlib import Path

from executor import ToolExecutor
from schemas import PlanTask


def load_demo_plan(path: Path) -> list[PlanTask]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return [PlanTask(**task) for task in data["tasks"]]


def main() -> None:
    plan_path = Path(__file__).parent / "demo_plan.json"
    tasks = load_demo_plan(plan_path)
    result = ToolExecutor().run(tasks)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
