"""
AI Solution Recommender - Demo Project
Interactive CLI: takes your business requirements and recommends
the best AI model with platform info and free alternatives.
"""

import pandas as pd
import numpy as np

models = pd.DataFrame({
    'model': ['GPT-4o', 'Claude 3.5 Sonnet', 'Gemini 1.5 Pro', 'Llama 3 70B', 'Mistral Large'],
    'provider': ['OpenAI', 'Anthropic', 'Google', 'Meta', 'Mistral'],
    'open_source': [False, False, False, True, True],
    'coding': [90, 92, 84, 80, 82],
    'reasoning': [89, 91, 86, 83, 84],
    'creative': [88, 85, 82, 76, 78],
    'analysis': [87, 90, 88, 81, 83],
    'multilingual': [85, 82, 91, 78, 80],
    'vision': [92, 88, 87, 0, 0],
    'cost_monthly': [200, 150, 120, 30, 80],
    'latency': [1.2, 1.5, 0.8, 2.0, 1.0],
    'privacy_score': [2, 3, 2, 5, 4],
    'ease_integration': [5, 4, 4, 3, 3],
    'reliability': [95, 93, 90, 85, 88],
})

platforms = {
    'GPT-4o': {
        'api': 'OpenAI API (platform.openai.com)',
        'web': 'ChatGPT (chatgpt.com)',
        'free_tier': False,
        'self_host': False,
    },
    'Claude 3.5 Sonnet': {
        'api': 'Anthropic API (console.anthropic.com)',
        'web': 'Claude (claude.ai)',
        'free_tier': False,
        'self_host': False,
    },
    'Gemini 1.5 Pro': {
        'api': 'Google AI Studio (makersuite.google.com)',
        'web': 'Gemini (gemini.google.com)',
        'free_tier': True,
        'self_host': False,
    },
    'Llama 3 70B': {
        'api': 'Groq (groq.com), Replicate (replicate.com)',
        'web': 'Hugging Face Chat (huggingface.co/chat)',
        'free_tier': True,
        'self_host': True,
    },
    'Mistral Large': {
        'api': 'Mistral API (console.mistral.ai)',
        'web': 'Le Chat (chat.mistral.ai)',
        'free_tier': True,
        'self_host': True,
    },
}

free_alts = {
    'GPT-4o': 'Llama 3 70B',
    'Claude 3.5 Sonnet': 'Mistral Large',
    'Gemini 1.5 Pro': 'Mistral Large',
}

industries = {
    '1': 'E-commerce & Retail',
    '2': 'Healthcare & Pharma',
    '3': 'Finance & Banking',
    '4': 'Education & E-learning',
    '5': 'Marketing & Advertising',
    '6': 'Legal & Compliance',
    '7': 'Manufacturing & Supply Chain',
    '8': 'SaaS & Technology',
}

problems = {
    '1': ('Customer Support Chatbot', 'chatbot'),
    '2': ('Content Generation & Copywriting', 'content_gen'),
    '3': ('Data Analysis & Reporting', 'data_analysis'),
    '4': ('Code Generation & Review', 'code_gen'),
    '5': ('Document Processing & Summarization', 'document'),
    '6': ('Translation & Localization', 'translation'),
    '7': ('Text Classification & Routing', 'classification'),
    '8': ('Data Extraction & OCR', 'extraction'),
}

budget_levels = {
    '1': ('Low (under $100/mo)', 100),
    '2': ('Medium ($100-$200/mo)', 200),
    '3': ('High (unlimited)', 99999),
}

problem_weights = {
    'chatbot': {'reasoning': 0.3, 'multilingual': 0.2, 'latency': 0.2, 'cost_monthly': 0.15, 'reliability': 0.15},
    'content_gen': {'creative': 0.35, 'reasoning': 0.2, 'cost_monthly': 0.2, 'multilingual': 0.15, 'latency': 0.1},
    'data_analysis': {'analysis': 0.35, 'reasoning': 0.25, 'vision': 0.1, 'cost_monthly': 0.15, 'reliability': 0.15},
    'code_gen': {'coding': 0.4, 'reasoning': 0.2, 'latency': 0.1, 'cost_monthly': 0.15, 'reliability': 0.15},
    'document': {'analysis': 0.3, 'reasoning': 0.25, 'multilingual': 0.15, 'cost_monthly': 0.15, 'reliability': 0.15},
    'translation': {'multilingual': 0.4, 'reasoning': 0.2, 'cost_monthly': 0.2, 'latency': 0.1, 'reliability': 0.1},
    'classification': {'analysis': 0.3, 'reasoning': 0.2, 'cost_monthly': 0.2, 'reliability': 0.15, 'latency': 0.15},
    'extraction': {'vision': 0.3, 'analysis': 0.25, 'cost_monthly': 0.2, 'latency': 0.1, 'reliability': 0.15},
}


def print_platform(m):
    p = platforms.get(m)
    if not p:
        return
    print(f'    API: {p["api"]}')
    print(f'    Web: {p["web"]}')
    if p['free_tier']:
        print('    Free tier: Yes')
    if p['self_host']:
        print('    Self-hostable: Yes')


def recommend(problem_key, budget_max, data_sensitivity, tech_level):
    filtered = models.copy()
    if data_sensitivity == 'high':
        filtered['privacy_weight'] = filtered['privacy_score'] * 5
    else:
        filtered['privacy_weight'] = 3
    filtered = filtered[filtered['cost_monthly'] <= budget_max].copy()
    if len(filtered) == 0:
        print('  No models match your budget. Try a higher budget level.')
        return None
    w = problem_weights.get(problem_key, problem_weights['chatbot'])
    score_cols = ['coding', 'reasoning', 'creative', 'analysis', 'multilingual', 'vision']
    filtered['weighted'] = sum(filtered.get(c, 0) * w.get(c, 0) for c in score_cols)
    filtered['latency_penalty'] = filtered['latency'] / filtered['latency'].max()
    filtered['cost_penalty'] = 1 - (filtered['cost_monthly'].max() - filtered['cost_monthly']) / max(
        filtered['cost_monthly'].max() - filtered['cost_monthly'].min() + 1, 1)
    if tech_level == 'low':
        filtered['tech_score'] = filtered['ease_integration'] * 3
    else:
        filtered['tech_score'] = 3
    filtered['final'] = (filtered['weighted'] * 0.5 + filtered['reliability'] * 0.15 +
                         filtered['privacy_weight'] * 0.1 + filtered['tech_score'] * 0.1 -
                         filtered['latency_penalty'] * 0.08 - filtered['cost_penalty'] * 0.07)
    return filtered.sort_values('final', ascending=False)


def interactive():
    print('\n' + '=' * 60)
    print('  AI SOLUTION RECOMMENDER')
    print('  Answer a few questions about your business need.')
    print('=' * 60)
    print('\nSelect your industry:')
    for k, v in industries.items():
        print(f'  [{k}] {v}')
    while True:
        ind = input('\nIndustry (1-8): ').strip()
        if ind in industries:
            break
        print('  Invalid. Pick 1-8.')

    print(f'\nIndustry: {industries[ind]}')
    print('\nWhat problem are you solving?')
    for k, v in problems.items():
        print(f'  [{k}] {v[0]}')
    while True:
        prob = input('\nProblem (1-8): ').strip()
        if prob in problems:
            break
        print('  Invalid. Pick 1-8.')

    prob_label, prob_key = problems[prob]
    print(f'\nProblem: {prob_label}')

    print('\nBudget:')
    for k, v in budget_levels.items():
        print(f'  [{k}] {v[0]}')
    while True:
        bg = input('\nBudget (1-3): ').strip()
        if bg in budget_levels:
            break
        print('  Invalid. Pick 1-3.')
    _, budget_max = budget_levels[bg]

    print('\nHow technical is your team?')
    for k, v in [('1', 'Low (need easy integration)'), ('2', 'Medium'), ('3', 'High (can handle complex APIs)')]:
        print(f'  [{k}] {v}')
    tech = input('\nTechnical level (1-3): ').strip()
    tech_level = 'low' if tech == '1' else 'medium' if tech == '2' else 'high'

    data_sens = input('\nDo you handle sensitive data? (y/n): ').strip().lower()
    data_level = 'high' if data_sens == 'y' else 'low'

    result = recommend(prob_key, budget_max, data_level, tech_level)
    if result is None:
        return

    print('\n' + '-' * 60)
    print(f'  RECOMMENDATIONS FOR: {industries[ind]} | {prob_label}')
    print('-' * 60)
    for i, (_, row) in enumerate(result.head(3).iterrows()):
        tag = 'OPEN SOURCE' if row['open_source'] else 'PAID'
        print(f'\n  #{i+1}: {row["model"]} ({row["provider"]}) [{tag}]')
        print(f'    Score: {row["final"]:.1f} | Cost: ${row["cost_monthly"]}/mo | Latency: {row["latency"]}s')
        print_platform(row['model'])
        alt = free_alts.get(row['model'])
        if alt:
            alt_data = models[models['model'] == alt].iloc[0]
            print(f'    >> Free alternative: {alt} (${alt_data["cost_monthly"]}/mo, open source)')
            print_platform(alt)

        reasons = []
        if row['open_source']:
            reasons.append('Self-hostable (data stays on premise)')
        if row['coding'] > 85:
            reasons.append('Strong coding capability')
        if row['reasoning'] > 85:
            reasons.append('Advanced reasoning')
        if row['vision'] > 80:
            reasons.append('Vision/multimodal support')
        for r in reasons:
            print(f'    -> {r}')

    print(f'\n  Full ranking:')
    for _, row in result.iterrows():
        tag = 'FREE' if row['open_source'] else 'PAID'
        print(f'    {row["model"]:25s} score: {row["final"]:.1f}  ${row["cost_monthly"]:>3}/mo  [{tag}]')

    print('\n  BEST VALUE PICK:')
    best_val = result.iloc[0]
    alt = free_alts.get(best_val['model'])
    if alt:
        print(f'    Paid: {best_val["model"]} (${best_val["cost_monthly"]}/mo)')
        print(f'    Free: {alt} (${models[models["model"]==alt].iloc[0]["cost_monthly"]:.0f}/mo)')
        print(f'    Save ${best_val["cost_monthly"] - models[models["model"]==alt].iloc[0]["cost_monthly"]}/month')
    else:
        print(f'    Best option: {best_val["model"]} (already free / open source)')

    # Generate chart
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    scenarios = {
        'E-commerce Chatbot': {'problem': 'chatbot', 'budget': 100, 'tech': 'low', 'data': 'low'},
        'Healthcare Docs': {'problem': 'document', 'budget': 99999, 'tech': 'high', 'data': 'high'},
        'SaaS Code Gen': {'problem': 'code_gen', 'budget': 99999, 'tech': 'high', 'data': 'medium'},
        'Marketing Content': {'problem': 'content_gen', 'budget': 200, 'tech': 'medium', 'data': 'low'},
    }
    for ax, (sn, si) in zip(axes.flat, scenarios.items()):
        r = recommend(si['problem'], si['budget'], si['data'], si['tech'])
        if r is not None:
            colors = ['#2ecc71' if i < 3 else '#95a5a6' for i in range(len(r))]
            ax.barh(r['model'], r['final'], color=colors)
            ax.set_title(sn)
            ax.set_xlabel('Score')
            ax.set_xlim(0, 100)
            for i, v in enumerate(r['final']):
                ax.text(v + 1, i, f'{v:.0f}', va='center', fontsize=9)
    plt.tight_layout()
    plt.savefig('ai_solution_recommender.png', dpi=150, bbox_inches='tight')
    print('\nSaved: ai_solution_recommender.png')
    models.to_csv('recommendation_output.csv', index=False)
    print('Exported: recommendation_output.csv')
    print('Done.')


if __name__ == '__main__':
    interactive()
