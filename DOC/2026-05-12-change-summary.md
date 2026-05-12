# 2026-05-12 變更說明

以下是今天在專案中的主要調整：

## 1) 套件化與入口整理
- 新增 `agent_learning_series` 套件結構，將核心功能集中於：
  - `intent/`：意圖分類
  - `routing/`：工具路由
  - `memory/`：session 記憶
- 新增 `agent_learning_series/cli.py` 作為整合式 CLI 主流程。
- 新增 `agent_learning_series/__main__.py`，支援：
  - `python -m agent_learning_series`
- 將 repo root 的 `main.py` 改為薄入口（呼叫套件 CLI）。

## 2) 可安裝化（Packaging）
- 新增 `pyproject.toml`，使專案可作為可安裝套件管理。
- README 補充安裝方式：
  - `pip install -e .`

## 3) 模組獨立執行相容性
- 更新以下既有 demo 入口：
  - `ai-agent-01-intent-understanding/app/main.py`
  - `ai-agent-02-tool-routing/app/main.py`
  - `ai-agent-03-session-memory/main.py`
- 移除 `sys.path` 硬改寫法，改為在未安裝套件時提供清楚提示訊息。

## 4) 測試補強
- 新增 `tests/test_intent_routing_memory.py`：
  - 驗證 intent 分類結果
  - 驗證 routing 工具選擇
  - 驗證 memory 更新與 summary 內容
- 新增 `tests/conftest.py` 測試環境路徑設定。

## 5) README 更新
- 補上 package refactor 後的執行說明：
  - 整合入口執行
  - 各模組單獨執行
  - 套件安裝與 `python -m` 方式

---
如需我再補一份「給團隊看的精簡版本（TL;DR）」或「部署/啟動 SOP」，我可以直接接著產出。
