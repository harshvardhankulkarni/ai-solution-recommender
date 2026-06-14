# Development: AI Solution Recommender

<!-- GSD -->

## Project Structure

All logic lives in `ai_solution_recommender.py` — a single-file application with no package layout. The file is organized as:

```
Lines    Section
------   -------
1-5      Module docstring
7-8      Imports (pandas, numpy)
10-25    models DataFrame — 5 model definitions with capability scores
27-58    platforms dict — access info per model
60-64    free_alts dict — paid -> free mapping
66-92    Input option dictionaries (industries, problems, budget_levels)
94-103   problem_weights dict — 8 weight profiles
105-116  print_platform() helper
118-141  recommend() — scoring engine
144-259  interactive() — CLI + visualization
262-263  Entry point guard
```

## How to Add New Models

### Step 1: Add to `models` DataFrame

Find the `models` DataFrame at line 10. Add a new row:

```python
{
    'model': 'Claude 3 Haiku',
    'provider': 'Anthropic',
    'open_source': False,
    'coding': 76,
    'reasoning': 79,
    'creative': 74,
    'analysis': 78,
    'multilingual': 75,
    'vision': 72,
    'cost_monthly': 25,
    'latency': 0.5,
    'privacy_score': 3,
    'ease_integration': 5,
    'reliability': 90,
}
```

### Step 2: Add platform info

Add an entry to the `platforms` dict (line 27):

```python
'Claude 3 Haiku': {
    'api': 'Anthropic API (console.anthropic.com)',
    'web': 'Claude (claude.ai)',
    'free_tier': False,
    'self_host': False,
},
```

### Step 3: (Optional) Add free alternative mapping

If the new model is paid and has an open-source alternative, add to `free_alts` (line 60):

```python
'Claude 3 Haiku': 'Llama 3 70B',
```

### Step 4: No other changes needed

The scoring engine, budget filter, and ranking logic operate on the full DataFrame. New models participate automatically.

## How to Modify Scoring Weights

### Global weights (line 138-140)

The final score formula in `recommend()`:

```python
filtered['final'] = (filtered['weighted'] * 0.5 +    # Task fit: 50%
                     filtered['reliability'] * 0.15 +  # Reliability: 15%
                     filtered['privacy_weight'] * 0.1 + # Privacy: 10%
                     filtered['tech_score'] * 0.1 -    # Ease of integration: 10%
                     filtered['latency_penalty'] * 0.08 - # Latency penalty: -8%
                     filtered['cost_penalty'] * 0.07)    # Cost penalty: -7%
```

Adjust any coefficient. Ensure the sum of positive weights plus penalties stays in a reasonable range.

### Per-problem weights (line 94-103)

Each problem type maps 5 capabilities to weights. Weights within a profile are independent (they do not need to sum to 1.0 — they multiply against capability scores which are 0-100).

To adjust a specific problem type, modify its entry in `problem_weights`:

```python
'chatbot': {'reasoning': 0.3, 'multilingual': 0.2, 'latency': 0.2, 'cost_monthly': 0.15, 'reliability': 0.15},
```

## How to Add Problem Types

### Step 1: Add a weight profile

Add to `problem_weights` (line 94):

```python
'sentiment': {'analysis': 0.3, 'reasoning': 0.25, 'cost_monthly': 0.2, 'multilingual': 0.15, 'reliability': 0.1},
```

### Step 2: Add to `problems` dict (line 77)

```python
'9': ('Sentiment Analysis', 'sentiment'),
```

### Step 3: Add to CLI menu

The CLI prints all keys in `problems` automatically — no code change needed for the menu loop.

## How to Add Industries

Simply add to the `industries` dict (line 66):

```python
'9': ('Government & Public Sector'),
```

Industries are informational only — they do not affect scoring.

## Code Style

- Single-file application. No classes.
- Function names: snake_case.
- Dictionaries and DataFrames defined at module level (globals).
- CLI uses numbered menus with validation loops.
- String formatting with f-strings.
- Matplotlib for static charts, Plotly for interactive charts (separate script).
- No type hints currently used.
