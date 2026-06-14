# Testing: AI Solution Recommender

<!-- GSD -->

## Automated Tests

None. The project is a single-file demo script with no test framework configured.

## Manual Validation

Run these checks after any change.

### 1. CLI Input Validation

| Test | Input | Expected behavior |
|------|-------|-------------------|
| Invalid industry | `9` at industry prompt | `Invalid. Pick 1-8.` — re-prompts |
| Invalid problem | `0` at problem prompt | `Invalid. Pick 1-8.` — re-prompts |
| Invalid budget | `4` at budget prompt | `Invalid. Pick 1-3.` — re-prompts |
| Non-numeric input | `abc` at any prompt | Python `ValueError` — script crashes (known limitation) |
| Budget low | Budget = 1 | Only models with cost_monthly ≤ $100 appear |
| Budget high | Budget = 3 | All 5 models appear |
| Sensitive data = y | `y` for data sensitivity | Privacy weight = privacy_score * 5 |
| Sensitive data = n | `n` for data sensitivity | Privacy weight = 3 |

### 2. Scoring Correctness

Run the CLI with various inputs and verify:

| Scenario | Expected top 3 observation |
|----------|---------------------------|
| Code generation, high budget | Claude 3.5 Sonnet scores high (92 coding) |
| Low budget ($100), chatbot | Mistral Large and Llama 3 70B rank above paid models |
| High data sensitivity | Llama 3 70B gets privacy boost (score 5) |
| Low tech level | Ease_integration-weighted models rise |
| Translation task | Gemini 1.5 Pro rises (multilingual 91) |

### 3. Scenario Comparison Chart

After CLI completes, verify `ai_solution_recommender.png`:
- Shows 4 bar charts in a 2x2 grid
- Each chart has a title (E-commerce Chatbot, Healthcare Docs, SaaS Code Gen, Marketing Content)
- Top 3 bars are green, remaining bars are gray
- Score values displayed on bars
- All 5 models visible in each scenario

### 4. CSV Export

Verify `recommendation_output.csv`:
- Contains all 5 model rows
- Headers match the DataFrame columns
- No empty cells
- Cost values are numeric

### 5. Interactive Chart

```bash
python generate_interactive.py
```

Verify `ai_solution_recommender_interactive.html`:
- Radar chart with 5 categories (Coding, Reasoning, Creative, Analysis, Multilingual)
- 5 traces with different colors, one per model
- Cost comparison bar chart below radar
- Hover tooltips work
- File opens in browser without errors

### 6. Regression: Budget Filter Edge Cases

Run `recommend()` directly (or simulate via CLI):

| Budget | Expected models in result |
|--------|--------------------------|
| $30 | Llama 3 70B only |
| $80 | Llama 3 70B, Mistral Large |
| $100 | Llama 3 70B, Mistral Large |
| $120 | Add Gemini 1.5 Pro |
| $150 | Add Claude 3.5 Sonnet |
| $200 | All 5 |
| $99999 | All 5 |

### 7. No-Model Boundary

Edit budget_max to $10 temporarily. Confirm the script prints:
```
No models match your budget. Try a higher budget level.
```

### 8. Free Alternative Mapping

| Paid model | Expected free alt |
|------------|-------------------|
| GPT-4o | Llama 3 70B |
| Claude 3.5 Sonnet | Mistral Large |
| Gemini 1.5 Pro | Mistral Large |

Llama 3 70B and Mistral Large (already free) should not have free alternatives shown.

## Test Matrix (Quick Reference)

Run this combination matrix when modifying the scoring engine:

| Industry | Problem | Budget | Tech | Data sens | Expected pattern |
|----------|---------|--------|------|-----------|-----------------|
| Any | code_gen | high | high | n | Claude 3.5 Sonnet #1 |
| Any | chatbot | low | low | n | Mistral or Llama top |
| Any | translation | high | medium | n | Gemini 1.5 Pro strong |
| Healthcare | document | high | high | y | Claude 3.5 Sonnet or Llama |
| Any | code_gen | low | high | n | Only Llama 3 70B returned |
