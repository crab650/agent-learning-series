from app.intent_classifier import IntentClassifier


def main():
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