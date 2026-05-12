from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class PlanTask:
    step: int
    action: str
    input: dict[str, Any] = field(default_factory=dict)
    depends_on: list[int] = field(default_factory=list)


@dataclass
class StepResult:
    step: int
    action: str
    status: str
    output: dict[str, Any] | None = None
    error: str | None = None
    skipped_reason: str | None = None
