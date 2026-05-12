import sys


def _configure_console_encoding() -> None:
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")


def main():
    _configure_console_encoding()
    try:
        from agent_learning_series.intent import IntentClassifier
    except ModuleNotFoundError:
        print("找不到 agent_learning_series 套件，請先在 repo 根目錄執行：pip install -e .")
        return

    classifier = IntentClassifier()

    print("Intent Understanding Demo")
    print("Type 'exit' to quit.\n")

    while True:
        query = input("User> ").strip()
        if query.lower() == "exit":
            break

        result = classifier.classify(query)

        print("\nResult:")
        print(f"  query      : {result.query}")
        print(f"  intent     : {result.intent}")
        print(f"  confidence : {result.confidence}")
        print(f"  matched_by : {result.matched_by}")
        print(f"  reason     : {result.reason}")
        print()


if __name__ == "__main__":
    main()
