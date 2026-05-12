from dataclasses import asdict
import sys

from agent_learning_series.intent import IntentClassifier
from agent_learning_series.memory import handle_user_message, load_session, save_session
from agent_learning_series.routing import route_tools


def _configure_console_encoding() -> None:
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")


def main() -> None:
    _configure_console_encoding()
    session_id = input("請輸入 session_id（直接 Enter 預設 user001）: ").strip() or "user001"
    session = load_session(session_id)
    classifier = IntentClassifier()

    print("Agent Learning Series 整合入口")
    print("輸入 exit 離開，show 顯示記憶摘要。\n")

    while True:
        query = input("You> ").strip()
        if not query:
            continue
        if query.lower() == "exit":
            save_session(session)
            print("Session 已儲存，掰掰。")
            break
        if query.lower() == "show":
            print(session["session_summary"]["summary"])
            print(session["working_memory"])
            continue

        intent = classifier.classify(query)
        routing = route_tools(query)
        session = handle_user_message(session, query)
        save_session(session)

        print("\n[Intent]")
        print(asdict(intent))
        print("\n[Routing]")
        print(asdict(routing))
        print("\n[Memory Reply]")
        print(session["raw_messages"][-1]["content"])
        print()
