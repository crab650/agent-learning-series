from typing import Any, Dict

from memory import update_working_memory, update_user_profile
from session_store import append_message
from summarizer import update_session_summary


def build_reply(session: Dict[str, Any], user_text: str) -> str:
    wm = session["working_memory"]
    summary = session["session_summary"]["summary"]

    lines = []
    lines.append("我已更新這次 session 記憶。")

    if wm.get("current_material"):
        lines.append(f"- current_material: {wm['current_material']}")
    if wm.get("current_topic"):
        lines.append(f"- current_topic: {wm['current_topic']}")
    if wm.get("last_time_reference"):
        lines.append(f"- last_time_reference: {wm['last_time_reference']}")
    if wm.get("current_intent"):
        lines.append(f"- current_intent: {wm['current_intent']}")

    lines.append(f"- summary: {summary}")

    return "\n".join(lines)


def handle_user_message(session: Dict[str, Any], user_text: str) -> Dict[str, Any]:
    append_message(session, "user", user_text)

    update_working_memory(session, user_text)
    update_user_profile(session, user_text)
    update_session_summary(session)

    reply = build_reply(session, user_text)
    append_message(session, "assistant", reply)

    return session