from agent import handle_user_message
from session_store import load_session, save_session


def main() -> None:
    session_id = input("請輸入 session_id（直接 Enter 預設 user001）: ").strip()
    if not session_id:
        session_id = "user001"

    session = load_session(session_id)

    print(f"已載入 session: {session_id}")
    print("輸入 exit 離開，輸入 show 查看目前 session 摘要。\n")

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            continue

        if user_input.lower() == "exit":
            save_session(session)
            print("Session 已儲存，程式結束。")
            break

        if user_input.lower() == "show":
            print("\n=== Session Summary ===")
            print(session["session_summary"]["summary"])
            print("\n=== Working Memory ===")
            print(session["working_memory"])
            print()
            continue

        session = handle_user_message(session, user_input)
        save_session(session)

        last_reply = session["raw_messages"][-1]["content"]
        print(f"AI:\n{last_reply}\n")


if __name__ == "__main__":
    main()