import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import mannwhitneyu

# Ler o arquivo CSV
data = pd.read_csv('out/results.csv')

# Filtrar os dados para cada tipo
data_graphql = data[data['api'] == 'graphql']
data_rest = data[data['api'] == 'rest']

# Criar uma lista de dados para o boxplot
data_list = [data_graphql['elapsed_time'], data_rest['elapsed_time']]

# Criar um subplot para o boxplot
fig, ax = plt.subplots()

# Criar o boxplot
ax.boxplot(data_list, labels=['GraphQL', 'REST'])

# Calcular as medianas para cada tipo de API
median_graphql = data_graphql['elapsed_time'].median()
median_rest = data_rest['elapsed_time'].median()

# Adicionar linhas horizontais para representar as medianas
ax.axhline(y=median_graphql, color='red', linestyle='--', label=f'Mediana - GraphQL: {median_graphql:.2f}')
ax.axhline(y=median_rest, color='blue', linestyle='--', label=f'Mediana - REST: {median_rest:.2f}')

# Realizar o teste de Mann-Whitney
statistic, p_value = mannwhitneyu(data_graphql['elapsed_time'], data_rest['elapsed_time'])
alpha = 0.05

# Adicionar o resultado do teste de Mann-Whitney no gráfico
if p_value < alpha:
    ax.text(0.5, 0.05, f'Teste de Mann-Whitney: p-value = {p_value:.4f} (diferentes)', transform=ax.transAxes,
            fontsize=10, verticalalignment='bottom', horizontalalignment='center', bbox=dict(facecolor='red', alpha=0.5))
else:
    ax.text(0.5, 0.05, f'Teste de Mann-Whitney: p-value = {p_value:.4f} (sem diferença)', transform=ax.transAxes,
            fontsize=10, verticalalignment='bottom', horizontalalignment='center', bbox=dict(facecolor='green', alpha=0.5))

# Adicionar título e rótulos aos eixos
ax.set_title('Boxplot - elapsed_time')
ax.set_xlabel('Type')
ax.set_ylabel('Body Size')

# Mostrar a legenda
ax.legend()

# Mostrar o boxplot
plt.show()
