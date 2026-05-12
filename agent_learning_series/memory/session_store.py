import json
from datetime import datetime
from pathlib import Path

SESSION_DIR = Path("ai-agent-03-session-memory/sessions")

def _now_iso() -> str:
    return datetime.now().isoformat(timespec="seconds")

def _get_session_path(session_id: str) -> Path:
    SESSION_DIR.mkdir(parents=True, exist_ok=True)
    return SESSION_DIR / f"{session_id}.json"

def create_empty_session(session_id: str) -> dict:
    now = _now_iso()
    return {
        "session_id": session_id,
        "created_at": now,
        "updated_at": now,
        "raw_messages": [],
        "working_memory": {
            "current_material": None,
            "current_topic": None,
            "last_time_reference": None,
            "current_intent": None,
        },
        "user_profile": {
            "preferred_language": "zh-TW",
            "name": None,
            "company": None,
            "role": None,
            "common_topics": [],
        },
        "session_summary": {"summary": ""},
    }

def load_session(session_id: str) -> dict:
    path = _get_session_path(session_id)
    if not path.exists():
        session = create_empty_session(session_id)
        save_session(session)
        return session
    return json.loads(path.read_text(encoding="utf-8"))

def save_session(session: dict) -> None:
    session["updated_at"] = _now_iso()
    path = _get_session_path(session["session_id"])
    path.write_text(json.dumps(session, ensure_ascii=False, indent=2), encoding="utf-8")

def append_message(session: dict, role: str, content: str) -> None:
    session["raw_messages"].append({"role": role, "content": content, "timestamp": _now_iso()})
