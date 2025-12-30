# Copilot Instructions

- **Project scope**: Notebook-first quant research lab exploring agentic AI for fundamentals + technical signals; workflow outline in [README.md](README.md#L1-L75).
- **Current code**: [main.py](main.py#L1-L6) only prints a greeting; real work is expected to live in notebooks and the `utils` package.
- **Planned pipeline** (per README): Universe/Data → Feature engineering → Strategy design → Backtesting → Agentic evaluation; keep new code aligned with these phases.
- **Notebooks**: Workbooks under `notebooks/` (00–05) follow the above pipeline; keep heavy logic in Python modules so notebooks stay orchestration/visualization-focused.
- **Utilities**: Scaffold modules exist but are empty: [utils/backtest.py](utils/backtest.py), [utils/fundamentals.py](utils/fundamentals.py), [utils/indicators.py](utils/indicators.py), [utils/metrics.py](utils/metrics.py). Implement reusable functions here instead of inside notebooks.
- **Data & outputs**: `data/` for inputs, `reports/` for markdown summaries (performance, risk, strategy), `assets/` for static images used by the README.
- **Dependencies & runtime**: Python >=3.13 with only `openai` and `python-dotenv` declared in [pyproject.toml](pyproject.toml#L1-L8); install via `pip install -e .` or `pip install .` before running notebooks.
- **LLM/agent frameworks**: README lists LangGraph, CrewAI, multiple LLM vendors, but they are not yet dependencies—add them explicitly before use and gate any vendor-specific code behind environment variables loaded via `dotenv`.
- **Execution**: `python main.py` is currently a sanity check; primary workflow is running notebooks in order (00→05). Prefer deterministic cells and lightweight notebook outputs to keep diffs small.
- **Conventions**: Keep new code ASCII-only; structure helpers by domain (backtesting, fundamentals, indicators, metrics) to make strategies composable; surface configurable parameters clearly for experimentation.
- **Docs**: Update [README.md](README.md#L1-L75) checklists when major phases become implemented; keep report files in `reports/` in sync with experiment results.
- **Safety**: Project is research-only; avoid claims of financial advice and preserve the disclaimer block in [README.md](README.md#L73-L75).
