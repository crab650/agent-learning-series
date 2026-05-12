from .memory import update_working_memory, update_user_profile
from .session_store import append_message
from .summarizer import update_session_summary


def build_reply(session: dict) -> str:
    wm = session["working_memory"]
    summary = session["session_summary"]["summary"]
    lines = ["我已更新這次 session 記憶。"]
    for field in ["current_material", "current_topic", "last_time_reference", "current_intent"]:
        if wm.get(field):
            lines.append(f"- {field}: {wm[field]}")
    lines.append(f"- summary: {summary}")
    return "\n".join(lines)

def handle_user_message(session: dict, user_text: str) -> dict:
    append_message(session, "user", user_text)
    update_working_memory(session, user_text)
    update_user_profile(session, user_text)
    update_session_summary(session)
    append_message(session, "assistant", build_reply(session))
    return session
