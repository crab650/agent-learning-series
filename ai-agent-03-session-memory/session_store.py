import json
import os
from datetime import datetime
from typing import Any, Dict


SESSION_DIR = "sessions"


def ensure_session_dir() -> None:
    os.makedirs(SESSION_DIR, exist_ok=True)


def now_iso() -> str:
    return datetime.now().isoformat(timespec="seconds")


def get_session_path(session_id: str) -> str:
    ensure_session_dir()
    return os.path.join(SESSION_DIR, f"{session_id}.json")


def create_empty_session(session_id: str) -> Dict[str, Any]:
    now = now_iso()
    return {
        "session_id": session_id,
        "created_at": now,
        "updated_at": now,
        "raw_messages": [],
        "working_memory": {
            "current_material": None,
            "current_topic": None,
            "last_time_reference": None,
            "current_intent": None
        },
        "user_profile": {
            "preferred_language": "zh-TW",
            "name": None,
            "company": None,
            "role": None,
            "common_topics": []
        },
        "session_summary": {
            "summary": ""
        }
    }


def load_session(session_id: str) -> Dict[str, Any]:
    path = get_session_path(session_id)

    if not os.path.exists(path):
        session = create_empty_session(session_id)
        save_session(session)
        return session

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_session(session: Dict[str, Any]) -> None:
    session["updated_at"] = now_iso()
    path = get_session_path(session["session_id"])

    with open(path, "w", encoding="utf-8") as f:
        json.dump(session, f, ensure_ascii=False, indent=2)


def append_message(session: Dict[str, Any], role: str, content: str) -> None:
    session["raw_messages"].append({
        "role": role,
        "content": content,
        "timestamp": now_iso()
    })