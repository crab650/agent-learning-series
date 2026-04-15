import json
import sys
from dataclasses import asdict
from router import route_tools


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py \"你的問題\"")
        return

    query = sys.argv[1]
    result = route_tools(query)

    print(json.dumps(asdict(result), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()