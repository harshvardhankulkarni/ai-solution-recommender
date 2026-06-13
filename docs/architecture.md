# Architecture: AI Solution Recommender

## Context

Businesses face a difficult choice when selecting an AI model. Dozens of options exist with different strengths, costs, and trade-offs. A structured decision system helps match the right model to the right use case.

## Goals

- Accept client requirements in plain business terms.
- Score each model against weighted criteria.
- Return ranked recommendations with reasoning.
- Handle multiple industries and problem types.
- Produce a visual comparison across scenarios.

## Design

### System Architecture

```
Input Layer
  - Client requirements (industry, problem, budget, tech level, privacy, accuracy)
        |
        v
Filter Layer
  - Budget filter (removes models above price threshold)
  - Privacy filter (weighs open source for sensitive data)
  - Technical filter (weighs ease of integration for low-tech teams)
        |
        v
Scoring Engine
  - Task weights selected by problem type
  - Weighted score = sum(task_score * weight) for all capability dimensions
  - Final score = weighted_score*0.5 + reliability*0.15 + privacy*0.10 + tech*0.10 - latency*0.08 - cost*0.07
        |
        v
Ranking Layer
  - Sort by final score descending
  - Return top 3 with reasoning
        |
        v
Output Layer
  - Console report
  - Scenario visualization (multi-panel chart)
  - CSV export
```

### Model Capability Matrix

| Model | Coding | Reasoning | Creative | Analysis | Multilingual | Vision | Cost/mo | Latency |
|-------|--------|-----------|----------|----------|-------------|--------|---------|---------|
| GPT-4o | 90 | 89 | 88 | 87 | 85 | 92 | $200 | 1.2s |
| Claude 3.5 Sonnet | 92 | 91 | 85 | 90 | 82 | 88 | $150 | 1.5s |
| Gemini 1.5 Pro | 84 | 86 | 82 | 88 | 91 | 87 | $120 | 0.8s |
| Llama 3 70B | 80 | 83 | 76 | 81 | 78 | 0 | $30 | 2.0s |
| Mistral Large | 82 | 84 | 78 | 83 | 80 | 0 | $80 | 1.0s |

### Task Weight Profiles

Each problem type has a different weight profile. For example:

```python
'code_gen': {
    'coding_score': 0.4,       # Coding is 40% of the task score
    'reasoning_score': 0.2,
    'latency_sec': 0.1,
    'cost_monthly': 0.15,
    'reliability_score': 0.15,
}

'content_gen': {
    'creative_score': 0.35,    # Creative is 35% of the task score
    'reasoning_score': 0.2,
    'cost_monthly': 0.2,
    'multilingual_score': 0.15,
    'latency_sec': 0.1,
}
```

## Key Decisions

| Decision | Rationale |
|----------|-----------|
| Rule-based scoring instead of ML | Transparent, explainable, auditable. No training data needed. |
| 5 models | Covers the major providers (OpenAI, Anthropic, Google, Meta, Mistral). |
| 8 problem types | Covers 90% of common business AI use cases. |
| 6 input parameters | Enough to differentiate use cases without overwhelming users. |
| Weighted scoring | Simple additive model. Easy to understand and modify. |

## Trade-offs

- **Rule-based vs ML-based**: A machine learning model could learn better weights from historical decisions. Rule-based is simpler and more transparent but may miss subtle patterns.
- **5 vs 50 models**: 5 models is manageable for a demo. A production system would score 50+ models from an API.
- **Static weights**: Task weights are fixed. Real preferences vary by company, team, and project.
- **No financial ROI**: The system does not calculate expected ROI from using a specific model. That would require client-specific data.

## Integration Points

- **Input**: Dictionary of client requirements. Could come from a web form, API, or Slack command.
- **Output**: Structured recommendation data. Could feed into a web UI, report generator, or procurement system.
- **Extending**: Add new models by appending to the DataFrame. Add new problem types by defining weight profiles.

## Dependencies

- Python 3.8+
- pandas, numpy, matplotlib
