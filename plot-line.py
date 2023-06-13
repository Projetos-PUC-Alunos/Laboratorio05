import pandas as pd
import matplotlib.pyplot as plt

# Ler o arquivo CSV
data = pd.read_csv('out/results.csv')

# Filtrar os dados para cada tipo
data_graphql = data[data['api'] == 'graphql']
data_rest = data[data['api'] == 'rest']

# Calcular a mediana para cada tipo
median_graphql = data_graphql['elapsed_time'].median()
median_rest = data_rest['elapsed_time'].median()

# Criar o gráfico de barras comparativo
types = ['GraphQL', 'REST']
medians = [median_graphql, median_rest]

plt.bar(types, medians)

# Adicionar rótulos e título aos eixos
plt.xlabel('Tipo')
plt.ylabel('Mediana do elapsed_time')
plt.title('Comparativo da mediana do elapsed_time por tipo')

# Mostrar o gráfico
plt.show()
