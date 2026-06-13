# AI Solution Recommender - Demo Project

Recommends the best AI model for a given business use case. Evaluates 5 leading models across 10 capability dimensions against client requirements.

This is a demo project demonstrating a decision support system for AI model selection.

## How It Works

The system takes 6 client inputs:

| Input | Options | Description |
|-------|---------|-------------|
| Industry | ecommerce, healthcare, finance, education, marketing, legal, manufacturing, saas | Your business domain |
| Problem | chatbot, content_gen, data_analysis, code_gen, document, translation, classification, extraction | What you need AI to do |
| Budget | low (<$100/mo), medium (<$200/mo), high (any) | Monthly AI spend |
| Technical Level | low, medium, high | Your team ability to integrate AI |
| Data Sensitivity | low, medium, high | Privacy and compliance requirements |
| Accuracy Needed | low, medium, high | How critical is correctness |

## Models Evaluated

- GPT-4o (OpenAI)
- Claude 3.5 Sonnet (Anthropic)
- Gemini 1.5 Pro (Google)
- Llama 3 70B (Meta, open source)
- Mistral Large (Mistral, open source)

## Scoring Dimensions

| Dimension | Weight | Description |
|-----------|--------|-------------|
| Task Fit Score | 50% | How well the model performs on the specific task type (coding, reasoning, creative, analysis, multilingual, vision) |
| Reliability | 15% | Uptime, consistency, track record |
| Privacy | 10% | Data handling, on-premise capability |
| Ease of Integration | 10% | API quality, documentation, SDK support |
| Latency Penalty | -8% | Slower models lose points |
| Cost Penalty | -7% | More expensive models lose points |

## Sample Scenarios

| Scenario | Top Pick | Why |
|----------|----------|-----|
| E-commerce chatbot (low budget) | Gemini 1.5 Pro | Low cost, fast, multilingual |
| Healthcare document analysis (high privacy) | Llama 3 70B | Open source, self-hosted, data stays on premise |
| SaaS code generation | Claude 3.5 Sonnet | Best coding scores (92%), advanced reasoning |
| Marketing content (global audience) | GPT-4o | Strong creative + multilingual, easy integration |

## How to Run

```bash
pip install pandas matplotlib numpy
python ai_solution_recommender.py
```

Output: `ai_solution_recommender.png` (4-panel scenario chart) and recommendation CSVs.

## Tech Stack

Python, Pandas, NumPy, Matplotlib

## License

MIT
