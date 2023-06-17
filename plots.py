import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import spearmanr

# Ler o arquivo CSV
data = pd.read_csv('out/results.csv')

# Filtrar os dados para cada tipo
data_graphql = data[data['api'] == 'graphql']
data_rest = data[data['api'] == 'rest']

# Calcular o coeficiente de correlação de Spearman
correlation, _ = spearmanr(data_graphql['elapsed_time'], data_rest['elapsed_time'])

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

# Adicionar título e rótulos aos eixos
ax.set_title('Boxplot - elapsed_time')
ax.set_xlabel('Type')
ax.set_ylabel('Elapsed Time')

# Mostrar o coeficiente de correlação de Spearman
ax.text(0.5, 0.05, f'Coeficiente de Spearman: {correlation:.2f}', transform=ax.transAxes, ha='center')

# Mostrar a legenda
ax.legend()

# Mostrar o boxplot
plt.show()
