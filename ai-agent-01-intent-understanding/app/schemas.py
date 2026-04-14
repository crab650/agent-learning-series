from dataclasses import dataclass


@dataclass
class IntentResult:
    query: str
    intent: str
    confidence: float
    matched_by: str
    reason: str