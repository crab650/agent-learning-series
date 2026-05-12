# 📦 ai-agent-05-tool-execution

## 🔹 專案簡介

本模組將 `ai-agent-04-task-planning` 產生的任務計畫真正執行，包含：

- 依步驟順序執行工具
- 檢查 `depends_on` 相依關係
- 工具錯誤隔離與狀態回報
- 統一輸出 execution report

## 🧠 核心能力

1. **Tool Registry**：將 `action` 對應到實作函式。  
2. **Dependency-aware Execution**：僅在相依步驟成功時執行下一步。  
3. **Fault Handling**：支援 unknown action、exception、dependency fail。  
4. **Structured Output**：提供 `step_results` + `final_status` 供後續 response synthesis。

## ▶️ 執行方式

```bash
python ai-agent-05-tool-execution/main.py
```

## 📤 輸出範例

- `success`: 所有步驟成功
- `partial_success`: 部分成功，部分失敗或跳過
- `failed`: 全部失敗
- `skipped`: 全部跳過

## 📁 檔案說明

- `schemas.py`：任務與結果資料模型
- `tools.py`：mock 工具實作
- `executor.py`：執行引擎
- `demo_plan.json`：示範任務計畫
- `main.py`：demo 入口
