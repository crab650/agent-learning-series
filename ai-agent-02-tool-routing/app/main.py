import json
import sys
from dataclasses import asdict


def main():
    try:
        from agent_learning_series.routing import route_tools
    except ModuleNotFoundError:
        print("找不到 agent_learning_series 套件，請先在 repo 根目錄執行：pip install -e .")
        return

    if len(sys.argv) < 2:
        print('Usage: python main.py "你的問題"')
        return

    query = sys.argv[1]
    result = route_tools(query)

    print(json.dumps(asdict(result), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
