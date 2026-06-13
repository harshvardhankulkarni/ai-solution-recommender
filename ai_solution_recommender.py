"""
AI Solution Recommender - Demo Project
Recommends the best AI model for a given business use case.
Evaluates models against client requirements across multiple dimensions.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

models = pd.DataFrame({
    'model': ['GPT-4o', 'Claude 3.5 Sonnet', 'Gemini 1.5 Pro', 'Llama 3 70B', 'Mistral Large'],
    'provider': ['OpenAI', 'Anthropic', 'Google', 'Meta', 'Mistral'],
    'open_source': [False, False, False, True, True],
    'coding_score': [90, 92, 84, 80, 82],
    'reasoning_score': [89, 91, 86, 83, 84],
    'creative_score': [88, 85, 82, 76, 78],
    'analysis_score': [87, 90, 88, 81, 83],
    'multilingual_score': [85, 82, 91, 78, 80],
    'vision_score': [92, 88, 87, 0, 0],
    'cost_monthly': [200, 150, 120, 30, 80],
    'latency_sec': [1.2, 1.5, 0.8, 2.0, 1.0],
    'data_privacy': [2, 3, 2, 5, 4],
    'ease_integration': [5, 4, 4, 3, 3],
    'reliability_score': [95, 93, 90, 85, 88],
})

industries = {
    'ecommerce': 'E-commerce & Retail',
    'healthcare': 'Healthcare & Pharma',
    'finance': 'Finance & Banking',
    'education': 'Education & E-learning',
    'marketing': 'Marketing & Advertising',
    'legal': 'Legal & Compliance',
    'manufacturing': 'Manufacturing & Supply Chain',
    'saas': 'SaaS & Technology',
}

problem_types = {
    'chatbot': 'Customer Support Chatbot',
    'content_gen': 'Content Generation & Copywriting',
    'data_analysis': 'Data Analysis & Reporting',
    'code_gen': 'Code Generation & Review',
    'document': 'Document Processing & Summarization',
    'translation': 'Translation & Localization',
    'classification': 'Text Classification & Routing',
    'extraction': 'Data Extraction & OCR',
}

def recommend(client_input):
    industry = client_input['industry']
    problem = client_input['problem']
    budget = client_input['budget']
    technical = client_input['technical_level']
    data_sensitivity = client_input['data_sensitivity']
    accuracy_needed = client_input['accuracy_needed']

    scores = models.copy()

    # Limit open source for sensitive data
    if data_sensitivity == 'high':
        scores['privacy_score'] = scores['data_privacy'] * 5
    else:
        scores['privacy_score'] = 3

    # Budget filter
    if budget == 'low':
        scores = scores[scores['cost_monthly'] <= 100].copy()
    elif budget == 'medium':
        scores = scores[scores['cost_monthly'] <= 200].copy()

    # Technical capability filter
    if technical == 'low':
        scores['tech_score'] = scores['ease_integration'] * 3
    else:
        scores['tech_score'] = 3

    # Weight by problem type
    weights = {
        'chatbot': {'reasoning_score': 0.3, 'multilingual_score': 0.2, 'latency_sec': 0.2, 'cost_monthly': 0.15, 'reliability_score': 0.15},
        'content_gen': {'creative_score': 0.35, 'reasoning_score': 0.2, 'cost_monthly': 0.2, 'multilingual_score': 0.15, 'latency_sec': 0.1},
        'data_analysis': {'analysis_score': 0.35, 'reasoning_score': 0.25, 'vision_score': 0.1, 'cost_monthly': 0.15, 'reliability_score': 0.15},
        'code_gen': {'coding_score': 0.4, 'reasoning_score': 0.2, 'latency_sec': 0.1, 'cost_monthly': 0.15, 'reliability_score': 0.15},
        'document': {'analysis_score': 0.3, 'reasoning_score': 0.25, 'multilingual_score': 0.15, 'cost_monthly': 0.15, 'reliability_score': 0.15},
        'translation': {'multilingual_score': 0.4, 'reasoning_score': 0.2, 'cost_monthly': 0.2, 'latency_sec': 0.1, 'reliability_score': 0.1},
        'classification': {'analysis_score': 0.3, 'reasoning_score': 0.2, 'cost_monthly': 0.2, 'reliability_score': 0.15, 'latency_sec': 0.15},
        'extraction': {'vision_score': 0.3, 'analysis_score': 0.25, 'cost_monthly': 0.2, 'latency_sec': 0.1, 'reliability_score': 0.15},
    }

    w = weights.get(problem, weights['chatbot'])

    # Calculate weighted score
    score_cols = ['coding_score', 'reasoning_score', 'creative_score',
                  'analysis_score', 'multilingual_score', 'vision_score']
    scores['weighted_score'] = 0
    for col in score_cols:
        if col in w:
            scores['weighted_score'] += scores[col] * w[col]

    # Penalize high latency
    scores['latency_penalty'] = scores['latency_sec'] / scores['latency_sec'].max()
    scores['cost_penalty'] = 1 - (scores['cost_monthly'].max() - scores['cost_monthly']) / (scores['cost_monthly'].max() - scores['cost_monthly'].min() + 1)

    scores['final_score'] = (
        scores['weighted_score'] * 0.5 +
        scores['reliability_score'] * 0.15 +
        scores['privacy_score'] * 0.10 +
        scores['tech_score'] * 0.10 -
        scores['latency_penalty'] * 0.08 -
        scores['cost_penalty'] * 0.07
    )

    scores = scores.sort_values('final_score', ascending=False).reset_index(drop=True)
    scores['rank'] = range(1, len(scores) + 1)

    return scores

def run_scenario(client_input):
    print(f'\n=== RECOMMENDATION REPORT ===')
    print(f'Industry: {industries[client_input["industry"]]}')
    print(f'Problem: {problem_types[client_input["problem"]]}')
    print(f'Budget: {client_input["budget"].title()}')
    print(f'Technical Level: {client_input["technical_level"].title()}')
    print(f'Data Sensitivity: {client_input["data_sensitivity"].title()}')
    print(f'Accuracy Needed: {client_input["accuracy_needed"].title()}')

    result = recommend(client_input)

    print(f'\nTop 3 Recommendations:')
    for _, row in result.head(3).iterrows():
        fs = row['final_score']
        print(f'  #{int(row["rank"])}: {row["model"]} ({row["provider"]})')
        print(f'     Score: {fs:.1f} | Cost: ${row["cost_monthly"]}/mo | Latency: {row["latency_sec"]}s')
        msgs = []
        if row['open_source']:
            msgs.append('Self-hostable (data stays on premise)')
        if row['coding_score'] > 85:
            msgs.append('Strong coding capability')
        if row['reasoning_score'] > 85:
            msgs.append('Advanced reasoning')
        if row['vision_score'] > 80:
            msgs.append('Vision/multimodal support')
        for msg in msgs:
            print(f'     -> {msg}')

    print(f'\nAll Models Ranked:')
    for _, row in result.iterrows():
        print(f'  #{int(row["rank"])}: {row["model"]} ({row["final_score"]:.1f})')

    return result

# Scenario 1: E-commerce chatbot (low budget, non-technical)
ecom_chat = {
    'industry': 'ecommerce', 'problem': 'chatbot',
    'budget': 'low', 'technical_level': 'low',
    'data_sensitivity': 'low', 'accuracy_needed': 'medium'
}

# Scenario 2: Healthcare document analysis (high privacy, high accuracy)
healthcare_doc = {
    'industry': 'healthcare', 'problem': 'document',
    'budget': 'high', 'technical_level': 'high',
    'data_sensitivity': 'high', 'accuracy_needed': 'high'
}

# Scenario 3: SaaS code generation team
saas_code = {
    'industry': 'saas', 'problem': 'code_gen',
    'budget': 'high', 'technical_level': 'high',
    'data_sensitivity': 'medium', 'accuracy_needed': 'high'
}

# Scenario 4: Marketing content for global audience
marketing_content = {
    'industry': 'marketing', 'problem': 'content_gen',
    'budget': 'medium', 'technical_level': 'medium',
    'data_sensitivity': 'low', 'accuracy_needed': 'medium'
}

scenarios = {
    'E-commerce Chatbot': ecom_chat,
    'Healthcare Document Analysis': healthcare_doc,
    'SaaS Code Generation': saas_code,
    'Marketing Content': marketing_content,
}

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

for ax, (scenario_name, scenario_input) in zip(axes.flat, scenarios.items()):
    result = recommend(scenario_input)
    colors = ['#2ecc71' if i < 3 else '#95a5a6' for i in range(len(result))]
    ax.barh(result['model'], result['final_score'], color=colors)
    ax.set_title(scenario_name)
    ax.set_xlabel('Recommendation Score')
    ax.set_xlim(0, 100)
    for i, val in enumerate(result['final_score']):
        ax.text(val + 1, i, f'{val:.0f}', va='center', fontsize=9)

plt.tight_layout()
plt.savefig('ai_solution_recommender.png', dpi=150, bbox_inches='tight')
print('Saved: ai_solution_recommender.png')

# Run all scenarios
print('\n========================================')
print('AI SOLUTION RECOMMENDER - DEMO')
print('========================================')
for scenario_name, scenario_input in scenarios.items():
    result = run_scenario(scenario_input)

# Interactive mode
print('\n========================================')
print('CUSTOM SCENARIO MODE')
print('========================================')
print('You can modify the scenario variables below')
print('to test different business requirements.\n')

custom_input = {
    'industry': 'marketing',
    'problem': 'content_gen',
    'budget': 'medium',
    'technical_level': 'medium',
    'data_sensitivity': 'low',
    'accuracy_needed': 'high'
}

result = run_scenario(custom_input)

# Export
pd.DataFrame(scenarios.keys()).to_csv('scenarios_output.csv', index=False)
result.to_csv('recommendation_output.csv', index=False)
print('\nExported: scenarios_output.csv, recommendation_output.csv')
print('Done.\n')
