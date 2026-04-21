import re
from typing import Any, Dict


MATERIAL_PATTERN = re.compile(r"\b[A-Z]{2,}\d{2,}\b")


TOPIC_KEYWORDS = {
    "inventory": ["庫存", "存貨", "inventory", "stock"],
    "shipping": ["出貨", "ship", "shipping", "交貨"],
    "production": ["生產", "production", "製造"],
    "database": ["資料庫", "db", "database", "table", "schema"],
    "agent": ["agent", "session", "memory", "工具", "tool"]
}

TIME_KEYWORDS = {
    "today": ["今天", "today"],
    "yesterday": ["昨天", "yesterday"],
    "last_week": ["上週", "上个星期", "上個星期", "last week"],
    "last_month": ["上個月", "上个月", "last month"]
}

INTENT_KEYWORDS = {
    "query": ["查詢", "查一下", "看看", "查"],
    "compare": ["比較", "差異", "對比"],
    "analyze": ["分析", "原因", "為什麼"],
    "design": ["設計", "規劃", "架構"],
    "build": ["建立", "實作", "撰寫", "開發"]
}


def extract_material(text: str) -> str | None:
    match = MATERIAL_PATTERN.search(text.upper())
    return match.group(0) if match else None


def extract_topic(text: str) -> str | None:
    lower_text = text.lower()
    for topic, keywords in TOPIC_KEYWORDS.items():
        if any(keyword.lower() in lower_text for keyword in keywords):
            return topic
    return None


def extract_time_reference(text: str) -> str | None:
    lower_text = text.lower()
    for time_ref, keywords in TIME_KEYWORDS.items():
        if any(keyword.lower() in lower_text for keyword in keywords):
            return time_ref
    return None


def extract_intent(text: str) -> str | None:
    lower_text = text.lower()
    for intent, keywords in INTENT_KEYWORDS.items():
        if any(keyword.lower() in lower_text for keyword in keywords):
            return intent
    return None


def update_working_memory(session: Dict[str, Any], user_text: str) -> None:
    wm = session["working_memory"]

    material = extract_material(user_text)
    topic = extract_topic(user_text)
    time_ref = extract_time_reference(user_text)
    intent = extract_intent(user_text)

    if material:
        wm["current_material"] = material
    if topic:
        wm["current_topic"] = topic
    if time_ref:
        wm["last_time_reference"] = time_ref
    if intent:
        wm["current_intent"] = intent


def update_user_profile(session: Dict[str, Any], user_text: str) -> None:
    profile = session["user_profile"]
    lower_text = user_text.lower()

    if "繁中" in user_text or "繁體" in user_text:
        profile["preferred_language"] = "zh-TW"
    elif "簡中" in user_text or "简体" in user_text:
        profile["preferred_language"] = "zh-CN"
    elif "english" in lower_text or "英文" in user_text:
        profile["preferred_language"] = "en"

    topic = extract_topic(user_text)
    if topic and topic not in profile["common_topics"]:
        profile["common_topics"].append(topic)