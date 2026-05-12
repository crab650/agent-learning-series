from .rules import INTENT_RULES
from .schemas import IntentResult


class IntentClassifier:
    def __init__(self):
        self.rules = INTENT_RULES

    def classify(self, query: str) -> IntentResult:
        normalized_query = query.strip().lower()

        best_intent = None
        best_keyword = None
        best_score = 0

        for intent, keywords in self.rules.items():
            score = 0
            matched_keywords = []

            for kw in keywords:
                if kw.lower() in normalized_query:
                    score += 1
                    matched_keywords.append(kw)

            if score > best_score:
                best_score = score
                best_intent = intent
                best_keyword = matched_keywords

        if best_intent:
            confidence = min(0.5 + best_score * 0.2, 0.95)
            return IntentResult(
                query=query,
                intent=best_intent,
                confidence=confidence,
                matched_by="rule",
                reason=f"matched keywords: {best_keyword}",
            )

        return IntentResult(
            query=query,
            intent="unknown",
            confidence=0.2,
            matched_by="rule",
            reason="no keywords matched",
        )
