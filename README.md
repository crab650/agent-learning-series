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

## Notes

The `agent_learning_series/` package is the maintainable v2 structure. The original per-module folders are kept as standalone learning demos and historical checkpoints.
