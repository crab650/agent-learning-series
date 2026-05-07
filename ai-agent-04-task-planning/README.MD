# 📦 ai-agent-04-task-planning

## 🔹 專案簡介

本模組實現了一個 **具備 Task Planning 能力的 AI Agent**，  
使系統能將使用者的自然語言需求，轉換為 **可執行的多步任務流程（multi-step execution plan）**。

與前幾個模組相比，本階段的核心提升在於：

> ❗ Agent 不再只是「回應問題」，而是開始「規劃如何解決問題」

---

## 🧠 核心能力

### 1️⃣ Task Planning（任務拆解）

透過 LLM 將使用者輸入轉換為結構化任務：

```json
{
  "tasks": [
    {
      "step": 1,
      "action": "get_mes_finished_goods_inventory",
      "input": { "material_code": "CB602" },
      "depends_on": []
    },
    {
      "step": 2,
      "action": "get_raw_material_inventory",
      "input": { "material_code": "CB602" },
      "depends_on": []
    },
    {
      "step": 3,
      "action": "compare_inventory",
      "depends_on": [1, 2]
    }
  ]
}