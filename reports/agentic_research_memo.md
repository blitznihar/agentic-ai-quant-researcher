# Agentic Research Memo — Best Hybrid Candidate

**Question / Intent:** Find a robust hybrid strategy with low drawdown and reasonable turnover.  
**Router Decision:** risk_review  

## Selected Candidate
- **ID:** hyb_top15_th30_c0_t1
- **Top N (fundamental selection):** 15
- **Stochastic oversold threshold:** 30
- **Candle confirmation:** False
- **Trend filter (price > EMA20):** True

## Performance (Net of Costs)
- CAGR: 177.47%
- Sharpe: 6.03
- Sortino: 10.62
- Max Drawdown: -7.13%
- Calmar: 24.91
- Avg Turnover: 0.189

## Why this candidate won (Evaluator Summary)
- Optimizes risk-adjusted return (Sharpe) while controlling drawdown and turnover.
- Uses fundamentals for selection and technical signals for timing (reduces overtrading).

## Self-Reflection / Caveats
- Execution realism: if signals use close-of-day data, shift weights by +1 day before applying returns.
- Sparsity: portfolio invested on 93.2% of days.
- Concentration: average max single-name weight = 0.27 (lower is better).
- Turnover: avg daily turnover = 0.189.
- Holdings: avg names held = 5.0, median = 5.

## Next Improvements
- Shift weights by 1 day for strict execution realism.
- Add walk-forward splits and evaluate stability across regimes.
- Add sector constraints to reduce hidden concentration risk.
