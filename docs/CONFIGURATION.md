# Configuration: AI Solution Recommender

<!-- GSD -->

All configuration is inline in `ai_solution_recommender.py`. There are no external config files or environment variables.

## 1. Model Capability Scores

Location: `ai_solution_recommender.py:10-25`

5 models, each with 6 capability scores (0-100), cost, latency, privacy, ease_integration, and reliability.

| Model | Provider | Open | Cod | Reas | Creat | Anal | Multi | Vision | Cost | Lat | Priv | Ease | Rel |
|-------|----------|------|-----|------|-------|------|-------|--------|------|-----|------|------|-----|
| GPT-4o | OpenAI | No | 90 | 89 | 88 | 87 | 85 | 92 | $200 | 1.2s | 2 | 5 | 95 |
| Claude 3.5 Sonnet | Anthropic | No | 92 | 91 | 85 | 90 | 82 | 88 | $150 | 1.5s | 3 | 4 | 93 |
| Gemini 1.5 Pro | Google | No | 84 | 86 | 82 | 88 | 91 | 87 | $120 | 0.8s | 2 | 4 | 90 |
| Llama 3 70B | Meta | Yes | 80 | 83 | 76 | 81 | 78 | 0 | $30 | 2.0s | 5 | 3 | 85 |
| Mistral Large | Mistral | Yes | 82 | 84 | 78 | 83 | 80 | 0 | $80 | 1.0s | 4 | 3 | 88 |

Capabilities:
- `coding` — code generation and review proficiency
- `reasoning` — logical reasoning and problem-solving
- `creative` — creative writing and content generation
- `analysis` — data analysis and document understanding
- `multilingual` — non-English language support
- `vision` — image understanding and OCR (0 = not supported)

Other fields:
- `cost_monthly` — estimated monthly API cost in USD
- `latency` — average response time in seconds
- `privacy_score` — data privacy rating (1-5, higher = more private)
- `ease_integration` — API integration ease (1-5, higher = easier)
- `reliability` — uptime/consistency percentage (0-100)

## 2. Scoring Weights (Global)

Location: `ai_solution_recommender.py:138-140`

```
final = weighted * 0.50        # Task fit: 50%
      + reliability * 0.15     # Reliability: 15%
      + privacy_weight * 0.10  # Privacy: 10%
      + tech_score * 0.10      # Ease of integration: 10%
      - latency_penalty * 0.08 # Latency penalty: -8%
      - cost_penalty * 0.07   # Cost penalty: -7%
```

### Penalty formulas

```
latency_penalty = latency / max(latency)
  — normalized to the slowest model in the filtered set

cost_penalty = 1 - (max(cost) - cost) / (max(cost) - min(cost) + 1)
  — normalized rank cost penalty within the filtered set
```

### Conditional scores

```
if data_sensitivity == 'high':
    privacy_weight = privacy_score * 5
else:
    privacy_weight = 3

if tech_level == 'low':
    tech_score = ease_integration * 3
else:
    tech_score = 3
```

## 3. Problem Type Weight Profiles

Location: `ai_solution_recommender.py:94-103`

Each entry is `{capability: weight}`. These weights multiply against the corresponding 0-100 capability score in the weighted sum.

| Problem | Capability weights |
|---------|-------------------|
| chatbot | reasoning 0.3, multilingual 0.2, latency 0.2, cost 0.15, reliability 0.15 |
| content_gen | creative 0.35, reasoning 0.2, cost 0.2, multilingual 0.15, latency 0.1 |
| data_analysis | analysis 0.35, reasoning 0.25, vision 0.1, cost 0.15, reliability 0.15 |
| code_gen | coding 0.4, reasoning 0.2, latency 0.1, cost 0.15, reliability 0.15 |
| document | analysis 0.3, reasoning 0.25, multilingual 0.15, cost 0.15, reliability 0.15 |
| translation | multilingual 0.4, reasoning 0.2, cost 0.2, latency 0.1, reliability 0.1 |
| classification | analysis 0.3, reasoning 0.2, cost 0.2, reliability 0.15, latency 0.15 |
| extraction | vision 0.3, analysis 0.25, cost 0.2, latency 0.1, reliability 0.15 |

## 4. Budget Levels

Location: `ai_solution_recommender.py:88-92`

| Key | Label | Max cost/mo |
|-----|-------|-------------|
| 1 | Low (under $100/mo) | $100 |
| 2 | Medium ($100-$200/mo) | $200 |
| 3 | High (unlimited) | $99,999 |

## 5. Free Alternative Mapping

Location: `ai_solution_recommender.py:60-64`

| Paid model | Free alternative |
|------------|-----------------|
| GPT-4o | Llama 3 70B |
| Claude 3.5 Sonnet | Mistral Large |
| Gemini 1.5 Pro | Mistral Large |

Models not in this dict (`Llama 3 70B`, `Mistral Large`) are already free/open-source and do not map to an alternative.

## 6. Scenario Definitions (Visualization)

Location: `ai_solution_recommender.py:238-243`

4 hardcoded scenarios for the benchmark chart:

| Scenario | Problem | Budget | Tech | Data |
|----------|---------|--------|------|------|
| E-commerce Chatbot | chatbot | $100 | low | low |
| Healthcare Docs | document | unlimited | high | high |
| SaaS Code Gen | code_gen | unlimited | high | medium |
| Marketing Content | content_gen | $200 | medium | low |

## 7. Platform Access Info

Location: `ai_solution_recommender.py:27-58`

| Model | API | Web | Free tier | Self-host |
|-------|-----|-----|-----------|-----------|
| GPT-4o | OpenAI API (platform.openai.com) | ChatGPT (chatgpt.com) | No | No |
| Claude 3.5 Sonnet | Anthropic API (console.anthropic.com) | Claude (claude.ai) | No | No |
| Gemini 1.5 Pro | Google AI Studio (makersuite.google.com) | Gemini (gemini.google.com) | Yes | No |
| Llama 3 70B | Groq (groq.com), Replicate (replicate.com) | Hugging Face Chat (huggingface.co/chat) | Yes | Yes |
| Mistral Large | Mistral API (console.mistral.ai) | Le Chat (chat.mistral.ai) | Yes | Yes |
