import pandas as pd

# Ler o arquivo CSV
data = pd.read_csv('out/results.csv')

# Filtrar os dados para cada tipo
data_graphql = data[data['api'] == 'graphql']
data_rest = data[data['api'] == 'rest']

# Calcular medidas de tendência central para GraphQL
media_graphql = data_graphql['elapsed_time'].mean()
mediana_graphql = data_graphql['elapsed_time'].median()
moda_graphql = data_graphql['elapsed_time'].mode().iloc[0]

# Calcular medidas de variabilidade para GraphQL
desvio_padrao_graphql = data_graphql['elapsed_time'].std()
variancia_graphql = data_graphql['elapsed_time'].var()
valor_maximo_graphql = data_graphql['elapsed_time'].max()
valor_minimo_graphql = data_graphql['elapsed_time'].min()
obliquidade_graphql = data_graphql['elapsed_time'].skew()
curtose_graphql = data_graphql['elapsed_time'].kurtosis()

# Calcular medidas de tendência central para REST
media_rest = data_rest['elapsed_time'].mean()
mediana_rest = data_rest['elapsed_time'].median()
moda_rest = data_rest['elapsed_time'].mode().iloc[0]

# Calcular medidas de variabilidade para REST
desvio_padrao_rest = data_rest['elapsed_time'].std()
variancia_rest = data_rest['elapsed_time'].var()
valor_maximo_rest = data_rest['elapsed_time'].max()
valor_minimo_rest = data_rest['elapsed_time'].min()
obliquidade_rest = data_rest['elapsed_time'].skew()
curtose_rest = data_rest['elapsed_time'].kurtosis()

# Imprimir os resultados para GraphQL
print('Medidas de Tendência Central para GraphQL:')
print('Média:', media_graphql)
print('Mediana:', mediana_graphql)
print('Moda:', moda_graphql)
print('\nMedidas de Variabilidade para GraphQL:')
print('Desvio Padrão:', desvio_padrao_graphql)
print('Variância:', variancia_graphql)
print('Valor Máximo:', valor_maximo_graphql)
print('Valor Mínimo:', valor_minimo_graphql)
print('Obliquidade:', obliquidade_graphql)
print('Curtose:', curtose_graphql)

# Imprimir os resultados para REST
print('\nMedidas de Tendência Central para REST:')
print('Média:', media_rest)
print('Mediana:', mediana_rest)
print('Moda:', moda_rest)
print('\nMedidas de Variabilidade para REST:')
print('Desvio Padrão:', desvio_padrao_rest)
print('Variância:', variancia_rest)
print('Valor Máximo:', valor_maximo_rest)
print('Valor Mínimo:', valor_minimo_rest)
print('Obliquidade:', obliquidade_rest)
print('Curtose:', curtose_rest)
