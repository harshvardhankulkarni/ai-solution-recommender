# Runbook: AI Solution Recommender

## When to Use This Runbook

- Running the recommender for the first time.
- Creating custom business scenarios.
- Adding new models or problem types.
- Presenting recommendations to a client.

## Prerequisites

- Python 3.8+ installed.
- pip installed.

## Procedure

### Step 1: Install Dependencies

```bash
pip install pandas numpy matplotlib
```

### Step 2: Run the Default Scenarios

```bash
cd path/to/ai-solution-recommender
python ai_solution_recommender.py
```

### Step 3: Verify Output

Check for these files:

- `ai_solution_recommender.png` - 4-panel chart with scenario results.
- `scenarios_output.csv` - Scenario names.
- `recommendation_output.csv` - Scores for the custom scenario.

### Step 4: Review Recommendations

The console report shows for each scenario:

- Input parameters.
- Top 3 model recommendations with scores.
- Key strengths of each recommended model.
- Full ranking of all models.

## Running a Custom Scenario

### Step 1: Edit the Scenario

Open `ai_solution_recommender.py`. Find the `custom_input` dictionary near the bottom:

```python
custom_input = {
    'industry': 'marketing',
    'problem': 'content_gen',
    'budget': 'medium',
    'technical_level': 'medium',
    'data_sensitivity': 'low',
    'accuracy_needed': 'high'
}
```

### Step 2: Change Parameters

| Parameter | Options | Example |
|-----------|---------|---------|
| industry | ecommerce, healthcare, finance, education, marketing, legal, manufacturing, saas | 'finance' |
| problem | chatbot, content_gen, data_analysis, code_gen, document, translation, classification, extraction | 'code_gen' |
| budget | low, medium, high | 'low' |
| technical_level | low, medium, high | 'high' |
| data_sensitivity | low, medium, high | 'high' |
| accuracy_needed | low, medium, high | 'high' |

### Step 3: Run Again

```bash
python ai_solution_recommender.py
```

### Step 4: Use in Presentation

The console output is structured for easy copy-paste into a slide or report.

## Adding a New Model

### Step 1: Add Model Data

Add a row to the `models` DataFrame:

```python
{
    'model': 'Claude 3 Haiku',
    'provider': 'Anthropic',
    'open_source': False,
    'coding_score': 76,
    'reasoning_score': 79,
    'creative_score': 74,
    'analysis_score': 78,
    'multilingual_score': 75,
    'vision_score': 72,
    'cost_monthly': 25,
    'latency_sec': 0.5,
    'data_privacy': 3,
    'ease_integration': 5,
    'reliability_score': 90,
}
```

### Step 2: No Other Changes Needed

The scoring engine handles any number of models automatically.

## Adding a New Problem Type

### Step 1: Add a Weight Profile

Add to the `weights` dictionary:

```python
'sentiment': {
    'analysis_score': 0.30,
    'reasoning_score': 0.25,
    'multilingual_score': 0.20,
    'cost_monthly': 0.15,
    'reliability_score': 0.10,
}
```

### Step 2: Add to Problem Types

Add to the `problem_types` dictionary:

```python
'sentiment': 'Sentiment Analysis & Social Listening',
```

## Troubleshooting

| Problem | Cause | Fix |
|---------|-------|-----|
| No models returned | Budget filter removed all | Increase budget or add cheaper models |
| Wrong model ranked first | Weights do not match priorities | Adjust weight profile for the problem type |
| Score above 100 | Weight sum exceeds 1.0 | Check that weights sum to 1.0 per problem type |
| Cost value error | Missing or negative cost | Set cost_monthly to a positive value |
| All models tie | Capability scores are too similar | Increase score variance between models |

## Escalation

Open a GitHub issue with:

- Custom scenario parameters.
- Expected top recommendation.
- Actual output.
- Reasoning for disagreement with the result.
