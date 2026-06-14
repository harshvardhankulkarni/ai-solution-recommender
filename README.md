# AI Solution Recommender

<!-- GSD -->

Decision engine that recommends the best AI model for a given business use case. Answers 5 questions about your scenario and returns ranked recommendations with platform info, pricing, and free alternatives.

**Demo project** — part of the [data-analytics-portfolio](https://harshvardhankulkarni.github.io/data-analytics-portfolio/).

## Features

- Interactive CLI — 5 inputs, ranked output
- Multi-factor scoring engine (task fit, reliability, privacy, cost, latency)
- 5 models evaluated across 10 capability dimensions
- 8 industries and 8 problem types
- Free alternative mapping for every paid model
- 4-scenario benchmark comparison chart
- Interactive Plotly radar + cost chart

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Core engine | Python 3.8+ |
| Scoring & ranking | Pandas 2.0+, NumPy 1.24+ |
| Static visualization | Matplotlib 3.7+ |
| Interactive visualization | Plotly 5.15+ |
| GitHub Pages | Static HTML landing page |

## Quick Start

```bash
pip install pandas numpy matplotlib plotly

python ai_solution_recommender.py
```

Answer the 5 prompts. Results print to console. A scenario comparison chart saves as `ai_solution_recommender.png`.

## Project Structure

```
ai-solution-recommender/
  ai_solution_recommender.py     Main CLI + scoring engine
  ai_solution_recommender.ipynb  Notebook version
  generate_interactive.py        Plotly interactive chart generator
  index.html                     GitHub Pages landing page
  recommendation_output.csv      Custom scenario scores
  ai_solution_recommender.png    Scenario comparison chart
  ai_solution_recommender_interactive.html  Interactive Plotly chart
  README.md                      This file
  docs/
    ARCHITECTURE.md              System design and decisions
    GETTING-STARTED.md           Install and run guide
    DEVELOPMENT.md               Extension guide
    TESTING.md                   Manual validation
    CONFIGURATION.md             Scoring parameters reference
```

## Scoring Summary

| Factor | Weight | Description |
|--------|--------|-------------|
| Task fit | 50% | Weighted capability score for the selected problem type |
| Reliability | 15% | Uptime and consistency |
| Privacy | 10% | Data handling and on-premise capability |
| Ease of integration | 10% | API quality (weighted higher for low-tech teams) |
| Latency penalty | -8% | Normalized response time penalty |
| Cost penalty | -7% | Normalized monthly cost penalty |

## Links

- GitHub Pages: https://harshvardhankulkarni.github.io/ai-solution-recommender/
- Interactive chart: `ai_solution_recommender_interactive.html`
- Repository: https://github.com/harshvardhankulkarni/ai-solution-recommender
