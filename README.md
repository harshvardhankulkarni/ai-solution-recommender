# AI Solution Recommender - Demo Project

Recommends the best AI model for a given business use case. Evaluates 5 leading models across 10 capability dimensions against client requirements.

This is a demo project demonstrating a decision support system for AI model selection.

## Tech Stack

- Python 3.8+
- Pandas 2.0+ - Scoring and ranking engine
- NumPy 1.24+ - Numerical operations
- Matplotlib 3.7+ - Scenario visualization

## Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

```bash
git clone https://github.com/harshvardhankulkarni/ai-solution-recommender.git
cd ai-solution-recommender
pip install pandas numpy matplotlib
```

### Running

```bash
python ai_solution_recommender.py
```

Expected output:

```
========================================
AI SOLUTION RECOMMENDER - DEMO
========================================
=== RECOMMENDATION REPORT ===
Industry: E-commerce & Retail
Problem: Customer Support Chatbot
Budget: Low
Technical Level: Low
Data Sensitivity: Low
Accuracy Needed: Medium

Top 3 Recommendations:
  #1: Mistral Large (Mistral) - Score: 34.9
  #2: Llama 3 70B (Meta) - Score: 34.1
...
Exported: scenarios_output.csv, recommendation_output.csv
Done.
```

### Output Files

| File | Description |
|------|-------------|
| ai_solution_recommender.png | 4-scenario comparison chart |
| scenarios_output.csv | Scenario list |
| recommendation_output.csv | Full scores for custom scenario |

## How It Works

### Input Parameters

| Input | Options | What it controls |
|-------|---------|-----------------|
| industry | ecommerce, healthcare, finance, education, marketing, legal, manufacturing, saas | None (informational) |
| problem | chatbot, content_gen, data_analysis, code_gen, document, translation, classification, extraction | Task-specific weights |
| budget | low (<$100/mo), medium (<$200/mo), high (any) | Filters expensive models |
| technical_level | low, medium, high | Weighs ease of integration |
| data_sensitivity | low, medium, high | Weighs open source / privacy |
| accuracy_needed | low, medium, high | Adjusts accuracy requirements |

### Scoring System

The final score combines 6 factors:

| Factor | Weight | Description |
|--------|--------|-------------|
| Task Fit Score | 50% | How well the model performs on the specific task |
| Reliability | 15% | Uptime and consistency track record |
| Privacy Score | 10% | Data handling and on-premise capability |
| Ease of Integration | 10% | API quality and documentation |
| Latency Penalty | -8% | Slower models lose points |
| Cost Penalty | -7% | More expensive models lose points |

### Sample Scenarios

| Scenario | Top Pick | Why |
|----------|----------|-----|
| E-commerce chatbot (low budget) | Mistral Large | Open source, low cost, good reasoning |
| Healthcare document analysis (high privacy) | Claude 3.5 Sonnet | Best document analysis, strong privacy |
| SaaS code generation | Claude 3.5 Sonnet | Best coding (HumanEval 92%) |
| Marketing content (global) | GPT-4o | Strong creative + multilingual |

## Project Structure

```
ai-solution-recommender/
  ai_solution_recommender.py   Main recommendation engine
  README.md                    This file
  docs/
    architecture.md             Design and methodology
    runbook.md                  Operations guide with scenario builder
```

## Running Custom Scenarios

Edit the `custom_input` dictionary at the bottom of the script:

```python
custom_input = {
    'industry': 'healthcare',
    'problem': 'document',
    'budget': 'high',
    'technical_level': 'high',
    'data_sensitivity': 'high',
    'accuracy_needed': 'high'
}
```

Re-run the script to see the updated recommendations.

## License

MIT
