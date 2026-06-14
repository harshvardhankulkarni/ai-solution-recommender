
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

models_data = {
    'model': ['GPT-4o', 'Claude 3.5 Sonnet', 'Gemini 1.5 Pro', 'Llama 3 70B', 'Mistral Large'],
    'coding': [90, 92, 84, 80, 82],
    'reasoning': [89, 91, 86, 83, 84],
    'creative': [88, 85, 82, 76, 78],
    'analysis': [87, 90, 88, 81, 83],
    'multilingual': [85, 82, 91, 78, 80],
    'cost': [200, 150, 120, 30, 80],
}

df = pd.DataFrame(models_data)

fig = make_subplots(rows=2, cols=1,
    subplot_titles=('Model Capability Scores (Radar)', 'Cost Comparison'),
    specs=[[{'type': 'scatterpolar'}], [{'type': 'bar'}]])

categories = ['Coding', 'Reasoning', 'Creative', 'Analysis', 'Multilingual']
for i, row in df.iterrows():
    values = [row['coding'], row['reasoning'], row['creative'], row['analysis'], row['multilingual']]
    fig.add_trace(go.Scatterpolar(r=values + [values[0]], theta=categories + [categories[0]],
                                  fill='toself', name=row['model'],
                                  hovertemplate='%{theta}: %{r}<extra>%{name}</extra>'), row=1, col=1)

fig.add_trace(go.Bar(x=df['model'], y=df['cost'],
                     marker_color=['#e74c3c','#e67e22','#f39c12','#2ecc71','#3498db'],
                     text=[f'${c}/mo' for c in df['cost']],
                     textposition='outside', showlegend=False), row=2, col=1)

fig.update_layout(height=700, title_text='AI Solution Recommender - Interactive')
fig.write_html('ai_solution_recommender_interactive.html')
print('Saved: ai_solution_recommender_interactive.html')
