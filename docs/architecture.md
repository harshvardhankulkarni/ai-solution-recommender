<!-- GSD -->

# AI Solution Recommender — Architecture

## Context and Goals

Decision engine that matches AI models to business use cases. Interactive CLI takes 5 inputs (industry, problem type, budget, technical level, data sensitivity) and ranks models using a weighted scoring system.

## Data Flow

```
User Input (5 questions: industry, problem, budget, tech level, sensitivity)
  → Model filtering by budget/technical level
  → Multi-factor scoring (task fit 50%, reliability 15%, privacy 10%, integration 10%, latency -8%, cost -7%)
  → Ranking and top 3 recommendation
  → Free alternative mapping
  → 4-scenario comparison generation
  → Interactive Plotly radar chart + cost comparison
  → CSV export (recommendation, scenarios)
```

## Components

| File | Role |
|------|------|
| `ai_solution_recommender.py` | Main script: CLI interaction, scoring engine, ranking, scenario comparison, static chart |
| `generate_interactive.py` | Generates interactive Plotly HTML with radar + cost comparison |
| `ai_solution_recommender.ipynb` | Jupyter notebook for exploratory development |
| `recommendation_output.csv` | Custom scenario model scores |
| `scenarios_output.csv` | Scenario comparison data |
| `ai_solution_recommender.png` | Static 4-scenario comparison chart |
| `ai_solution_recommender_interactive.html` | Interactive Plotly chart |

## Scoring Model

| Factor | Weight | Notes |
|--------|--------|-------|
| Task fit | 50% | How well the model performs the specific problem type |
| Reliability | 15% | Consistency and uptime reputation |
| Privacy | 10% | Data handling and processing location |
| Ease of integration | 10% | API complexity and SDK availability |
| Latency penalty | -8% | Slow models penalized |
| Cost penalty | -7% | Expensive models penalized |

## Design Decisions

| Decision | Rationale |
|----------|-----------|
| 5 input questions | Captures key decision factors without overwhelming |
| Weighted scoring | Reflects real-world priority differences |
| Penalty factors | Latency and cost reduce but don't eliminate a model's chances |
| 4-scenario comparison | Shows how different inputs change recommendations |
| 5 models | Focused comparison on major providers |

## Trade-offs

- Scoring weights are subjective and business-dependent
- Limited model set may miss niche solutions
- No real-time model availability or pricing checks
- CLI only — no web UI or API

## File Organization

```
ai-solution-recommender/
├── ai_solution_recommender.py
├── generate_interactive.py
├── ai_solution_recommender.ipynb
├── ai_solution_recommender.png
├── ai_solution_recommender_interactive.html
├── recommendation_output.csv
├── scenarios_output.csv
├── index.html
└── docs/
    ├── ARCHITECTURE.md
    ├── GETTING-STARTED.md
    ├── DEVELOPMENT.md
    ├── TESTING.md
    └── CONFIGURATION.md
```
