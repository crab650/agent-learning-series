def generate_session_summary(session: dict) -> str:
    wm = session["working_memory"]
    messages = session["raw_messages"][-6:]
    recent_user_messages = [msg["content"] for msg in messages if msg["role"] == "user"]
    summary_parts = []
    if wm.get("current_material"):
        summary_parts.append(f"目前料號: {wm['current_material']}")
    if wm.get("current_topic"):
        summary_parts.append(f"目前主題: {wm['current_topic']}")
    if wm.get("last_time_reference"):
        summary_parts.append(f"時間參照: {wm['last_time_reference']}")
    if wm.get("current_intent"):
        summary_parts.append(f"目前意圖: {wm['current_intent']}")
    if recent_user_messages:
        summary_parts.append("最近使用者訊息: " + " | ".join(recent_user_messages))
    return "；".join(summary_parts) if summary_parts else "目前沒有摘要。"

def update_session_summary(session: dict) -> None:
    session["session_summary"]["summary"] = generate_session_summary(session)
