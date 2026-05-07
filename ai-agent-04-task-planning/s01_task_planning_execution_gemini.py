#!/usr/bin/env python3
"""
s01_task_planning_execution_gemini.py

Task Planning + Tool Execution Demo
使用 Gemini OpenAI-compatible API
"""

import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

MODEL = os.getenv("MODEL_ID", "gemini-2.5-flash")
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("Missing GEMINI_API_KEY in .env")

client = OpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# =========================
# 1. 模擬 Tools
# =========================

def get_mes_finished_goods_inventory(material_code: str):
    return {
        "material_code": material_code,
        "type": "finished_goods",
        "stock_qty": 1200,
        "warehouse": "FG-01",
        "location": "A-01"
    }


def get_raw_material_inventory(material_code: str):
    return {
        "material_code": material_code,
        "type": "raw_material",
        "stock_qty": 5300,
        "warehouse": "RM-02",
        "location": "B-03"
    }


def compare_inventory(data: list):
    return {
        "summary": "成品庫存 1200，原料庫存 5300，原料供應充足，但需確認成品是否能滿足近期出貨需求。"
    }


TOOLS = {
    "get_mes_finished_goods_inventory": get_mes_finished_goods_inventory,
    "get_raw_material_inventory": get_raw_material_inventory,
    "compare_inventory": compare_inventory,
}


# =========================
# 2. Task Planner
# =========================

PLANNER_SYSTEM = """
You are a task planner for an ERP / MES assistant.

Available actions are only:

1. get_mes_finished_goods_inventory
   - Use when user wants finished goods inventory.
   - input: {"material_code": "string"}

2. get_raw_material_inventory
   - Use when user wants raw material inventory.
   - input: {"material_code": "string"}

3. compare_inventory
   - Use when user wants comparison or analysis.
   - input: {}

Return JSON only.

JSON schema:
{
  "tasks": [
    {
      "step": 1,
      "action": "tool_name",
      "input": {},
      "depends_on": []
    }
  ]
}

Important:
- Return raw JSON only.
- Do not use markdown code fences.
- Do not write ```json.
- Do not add explanations.
"""


def clean_json_text(text: str) -> str:
    text = text.strip()

    if text.startswith("```json"):
        text = text.replace("```json", "", 1).strip()

    if text.startswith("```"):
        text = text.replace("```", "", 1).strip()

    if text.endswith("```"):
        text = text[:-3].strip()

    return text


def plan_tasks(user_input: str):
    messages = [
        {"role": "system", "content": PLANNER_SYSTEM},
        {"role": "user", "content": user_input}
    ]

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages
    )

    content = response.choices[0].message.content
    print("\n[LLM RAW CONTENT]")
    print(content)

    content = clean_json_text(content)

    try:
        return json.loads(content)
    except json.JSONDecodeError:
        print("\nLLM 回傳不是合法 JSON，清理後內容：")
        print(content)
        raise

# =========================
# 3. Tool Executor
# =========================

def execute_plan(plan: dict):
    results = {}

    for task in plan["tasks"]:
        step = task["step"]
        action = task["action"]
        task_input = task.get("input", {})

        print(f"\n[執行 Step {step}] {action}")

        if action not in TOOLS:
            results[step] = {
                "error": f"Unknown action: {action}"
            }
            continue

        tool_func = TOOLS[action]

        if action == "compare_inventory":
            dependency_results = [
                results[dep]
                for dep in task.get("depends_on", [])
                if dep in results
            ]
            output = tool_func(dependency_results)
        else:
            output = tool_func(**task_input)

        results[step] = output

        print(json.dumps(output, ensure_ascii=False, indent=2))

    return results


# =========================
# 4. Response Synthesizer
# =========================

SYNTHESIS_SYSTEM = """
You are an ERP / MES assistant.

Use the task plan and tool results to answer the user clearly.
Answer in Traditional Chinese.
Be concise but useful.
"""


def synthesize_response(user_input: str, plan: dict, results: dict):
    messages = [
        {"role": "system", "content": SYNTHESIS_SYSTEM},
        {
            "role": "user",
            "content": json.dumps({
                "user_input": user_input,
                "task_plan": plan,
                "tool_results": results
            }, ensure_ascii=False, indent=2)
        }
    ]

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages
    )

    return response.choices[0].message.content


# =========================
# 5. Main Loop
# =========================

def main():
    print("Task Planning Agent 啟動")
    print("輸入 exit 離開")

    while True:
        user_input = input("\nuser >> ")

        if user_input.lower() == "exit":
            break

        print("\n[1] 產生 Task Plan...")
        plan = plan_tasks(user_input)
        print(json.dumps(plan, ensure_ascii=False, indent=2))

        print("\n[2] 執行 Tools...")
        results = execute_plan(plan)

        print("\n[3] 統整回答...")
        final_answer = synthesize_response(user_input, plan, results)

        print("\nagent >>")
        print(final_answer)


if __name__ == "__main__":
    main()