# Getting Started: AI Solution Recommender

<!-- GSD -->

## Prerequisites

- Python 3.8 or higher
- pip package manager

## Installation

```bash
git clone https://github.com/harshvardhankulkarni/ai-solution-recommender.git
cd ai-solution-recommender
pip install pandas numpy matplotlib plotly
```

## Running the CLI Recommender

```bash
python ai_solution_recommender.py
```

You will see a welcome banner followed by 5 prompts.

## Understanding the 5 Questions

### 1. Industry (1-8)
Informational only. Used to label the output report. Does not affect scoring.

| Code | Industry |
|------|----------|
| 1 | E-commerce & Retail |
| 2 | Healthcare & Pharma |
| 3 | Finance & Banking |
| 4 | Education & E-learning |
| 5 | Marketing & Advertising |
| 6 | Legal & Compliance |
| 7 | Manufacturing & Supply Chain |
| 8 | SaaS & Technology |

### 2. Problem Type (1-8)
Selects the weight profile for scoring. Each problem type emphasizes different capabilities.

| Code | Problem | Key Capabilities |
|------|---------|-----------------|
| 1 | Customer Support Chatbot | reasoning (30%), multilingual (20%), latency (20%) |
| 2 | Content Generation & Copywriting | creative (35%), reasoning (20%), cost (20%) |
| 3 | Data Analysis & Reporting | analysis (35%), reasoning (25%), vision (10%) |
| 4 | Code Generation & Review | coding (40%), reasoning (20%), latency (10%) |
| 5 | Document Processing & Summarization | analysis (30%), reasoning (25%), multilingual (15%) |
| 6 | Translation & Localization | multilingual (40%), reasoning (20%), cost (20%) |
| 7 | Text Classification & Routing | analysis (30%), reasoning (20%), cost (20%) |
| 8 | Data Extraction & OCR | vision (30%), analysis (25%), cost (20%) |

### 3. Budget (1-3)
Filters out models whose `cost_monthly` exceeds the selected threshold.

| Code | Budget | Max cost/mo |
|------|--------|-------------|
| 1 | Low (under $100/mo) | $100 |
| 2 | Medium ($100-$200/mo) | $200 |
| 3 | High (unlimited) | No limit |

### 4. Technical Level (1-3)
Controls how much weight `ease_integration` receives.

| Code | Level | Effect |
|------|-------|--------|
| 1 | Low | `ease_integration * 3` added to score |
| 2 | Medium | No additional integration weight |
| 3 | High | No additional integration weight |

### 5. Data Sensitivity (y/n)
Controls privacy scoring.

| Response | Effect |
|----------|--------|
| y | `privacy_score * 5` added to score |
| n | Fixed +3 privacy contribution |

## Example Session

```
$ python ai_solution_recommender.py

============================================================
  AI SOLUTION RECOMMENDER
  Answer a few questions about your business need.
============================================================

Select your industry:
  [1] E-commerce & Retail
  [2] Healthcare & Pharma
  ...

Industry (1-8): 1
Industry: E-commerce & Retail

What problem are you solving?
  [1] Customer Support Chatbot
  [2] Content Generation & Copywriting
  ...

Problem (1-8): 1
Problem: Customer Support Chatbot

Budget:
  [1] Low (under $100/mo)
  [2] Medium ($100-$200/mo)
  [3] High (unlimited)

Budget (1-3): 1

How technical is your team?
  [1] Low (need easy integration)
  [2] Medium
  [3] High (can handle complex APIs)

Technical level (1-3): 1

Do you handle sensitive data? (y/n): n
```

## Expected Output

For each of the top 3 recommendations, you will see:
- Model name, provider, paid/open-source tag
- Score, monthly cost, latency
- API endpoint URL, web interface URL
- Free alternative (if available) with platform info
- Capability-based reasoning bullets

At the bottom:
- Full ranking of all models
- Best value pick (paid + free option with monthly savings)
- Saved chart: `ai_solution_recommender.png`
- Exported CSV: `recommendation_output.csv`

## Interactive Chart Version

Generate the Plotly interactive chart:

```bash
python generate_interactive.py
```

Opens `ai_solution_recommender_interactive.html` — a radar chart of model capabilities paired with a cost comparison bar chart. Hover for exact values.

## Output Files

| File | Description |
|------|-------------|
| `ai_solution_recommender.png` | 4-scenario comparison bar chart (E-commerce Chatbot, Healthcare Docs, SaaS Code Gen, Marketing Content) |
| `recommendation_output.csv` | Full model dataframe exported after your custom scenario run |
| `ai_solution_recommender_interactive.html` | Plotly interactive radar + cost chart |
