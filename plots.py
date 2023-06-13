import pandas as pd
import matplotlib.pyplot as plt

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

# Adicionar título e rótulos aos eixos
ax.set_title('Boxplot - elapsed_time')
ax.set_xlabel('Type')
ax.set_ylabel('Elapsed Time')

# Mostrar o boxplot
plt.show()
