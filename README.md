# AI Agent Learning Series

This repository is a hands-on learning project for building AI agent components with Python. Each module focuses on one capability in an agent workflow, from intent understanding to tool execution.

## Goal

Build a practical understanding of how AI agents work step by step:

- Intent understanding
- Tool routing
- Session memory
- Task planning
- Tool execution
- Response synthesis
- Tracing and observability
- End-to-end mini agent demo

## Project Structure

```text
.
|-- agent_learning_series/              # Refactored Python package
|-- ai-agent-01-intent-understanding/   # Rule-based intent classification
|-- ai-agent-02-tool-routing/           # Intent-to-tool routing
|-- ai-agent-03-session-memory/         # Session and working memory
|-- ai-agent-04-task-planning/          # Multi-step task planning
|-- ai-agent-05-tool-execution/         # Tool execution engine
|-- DOC/                                # Change notes and docs
|-- tests/                              # Integrated tests
|-- main.py                             # Integrated CLI entrypoint
`-- pyproject.toml                      # Package metadata
```

## Current Progress

- [x] `ai-agent-01-intent-understanding`
- [x] `ai-agent-02-tool-routing`
- [x] `ai-agent-03-session-memory`
- [x] `ai-agent-04-task-planning`
- [x] `ai-agent-05-tool-execution`
- [ ] `ai-agent-06-response-synthesis`
- [ ] `ai-agent-07-tracing-observability`
- [ ] `ai-agent-08-mini-agent-demo`

## Requirements

- Python 3.10+
- pip

The core package currently has no runtime dependencies.

## Installation

Install the package in editable mode:

```bash
pip install -e .
```

For development and testing:

```bash
pip install -e .[dev]
```

## Usage

Run the integrated CLI:

```bash
python main.py
```

Or run the package entrypoint:

```bash
python -m agent_learning_series
```

Inside the CLI:

- Type a user request to classify intent, route tools, and update memory.
- Type `show` to inspect the current memory summary.
- Type `exit` to save the session and quit.

Example query:

```text
查詢 CB602 成品庫存
```

## Run Module Demos

```bash
python ai-agent-01-intent-understanding/app/main.py
python ai-agent-02-tool-routing/app/main.py "查詢 CB602 成品庫存"
python ai-agent-03-session-memory/main.py
python ai-agent-05-tool-execution/main.py
```

## Testing

Run the test suite:

```bash
python -m pytest -q
```

Current tests cover:

- Intent classification
- Tool routing
- Session memory updates and summaries

## Testing Each Entry

Run these commands from the repository root.

| Target | Purpose | Test command |
| --- | --- | --- |
| Root `main.py` | Test the integrated CLI: intent, routing, and memory together. | `python main.py` |
| `agent_learning_series/` | Test the package entrypoint. | `python -m agent_learning_series` |
| `ai-agent-01-intent-understanding/` | Test rule-based intent classification. | `python ai-agent-01-intent-understanding/app/main.py` |
| `ai-agent-02-tool-routing/` | Test routing from user request to selected tools. | `python ai-agent-02-tool-routing/app/main.py "shipment CB602"` |
| `ai-agent-03-session-memory/` | Test session loading, working memory updates, and summary output. | `python ai-agent-03-session-memory/main.py` |
| `ai-agent-04-task-planning/` | Test LLM-based task planning and response synthesis. Requires Gemini API setup. | `python ai-agent-04-task-planning/s01_task_planning_execution_gemini.py` |
| `ai-agent-05-tool-execution/` | Test deterministic execution of `demo_plan.json`. | `python ai-agent-05-tool-execution/main.py` |
| `tests/` | Run automated integrated tests. | `python -m pytest -q` |

### Root Main Smoke Test

Manual test:

```bash
python main.py
```

Then enter:

```text
session_id: readme-smoke
You> shipment CB602 today
You> show
You> exit
```

PowerShell smoke test:

```powershell
@("readme-smoke", "shipment CB602 today", "show", "exit") | python main.py
```

Expected result:

- The program prints an intent result.
- The routing result includes `get_shipments`.
- The memory reply includes `current_material: CB602`.
- `show` displays the session summary and working memory.

### Module Smoke Tests

Intent understanding:

```powershell
@("check CB602 stock", "exit") | python ai-agent-01-intent-understanding/app/main.py
```

Expected result: intent should be `inventory_query`.

Tool routing:

```bash
python ai-agent-02-tool-routing/app/main.py "shipment CB602"
```

Expected result: selected tools should include `get_shipments`.

Session memory:

```powershell
@("memory-smoke", "check CB602 stock today", "show", "exit") | python ai-agent-03-session-memory/main.py
```

Expected result: working memory should include `current_material: CB602` and `last_time_reference: today`.

Task planning:

```bash
pip install openai python-dotenv
```

Set `GEMINI_API_KEY` in your environment or in a local `.env` file:

```text
GEMINI_API_KEY=your_api_key_here
MODEL_ID=gemini-2.5-flash
```

Then run:

```bash
python ai-agent-04-task-planning/s01_task_planning_execution_gemini.py
```

Expected result: the script prints a generated task plan, executes mock tools, and synthesizes a Traditional Chinese answer.

Tool execution:

```bash
python ai-agent-05-tool-execution/main.py
```

Expected result: final JSON output should include `"final_status": "success"`.

## Notes

The `agent_learning_series/` package is the maintainable v2 structure. The original per-module folders are kept as standalone learning demos and historical checkpoints.
