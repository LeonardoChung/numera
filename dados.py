import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configurações de plotagem
plt.rcParams.update({'font.size': 14, 'figure.figsize': (12, 8)})

# Carregar os dados
portfolio_df = pd.read_csv('portfolio_ofertas - portfolio_ofertas.csv', encoding='ISO-8859-1')
clientes_df = pd.read_csv('dados_clientes.csv', encoding='ISO-8859-1')
eventos_df = pd.read_csv('eventos_ofertas.csv', encoding='ISO-8859-1')

# Unir os dataframes
merged_df = pd.merge(eventos_df, portfolio_df, left_on='id_oferta', right_on='id')
merged_df = pd.merge(merged_df, clientes_df, left_on='cliente', right_on='id')
# Substituir valores NA pela mediana
merged_df['valor'].fillna(merged_df['valor'].median(), inplace=True)

# Análise descritiva dos clientes
print(clientes_df.describe())

# Análise das ofertas
ofertas = merged_df['oferta'].value_counts()
ofertas.plot(kind='bar')
plt.title('Número de Ofertas por Tipo')
plt.xlabel('Tipo de Oferta')
plt.ylabel('Número de Ofertas')
plt.xticks(rotation=0)  # Rótulos do eixo x agora estão horizontais
plt.show()

# Análise de canais de comunicação
canais = merged_df['canal'].value_counts()
canais.plot(kind='bar')
plt.title('Número de Comunicações por Canal')
plt.xlabel('Canal de Comunicação')
plt.ylabel('Número de Comunicações')
plt.xticks(rotation=0)
plt.show()


# Análise descritiva dos eventos
print(eventos_df.describe())

# Contagem de cada tipo de evento
eventos = eventos_df['tipo_evento'].value_counts()
eventos.plot(kind='bar')
plt.title('Número de Eventos por Tipo')
plt.xlabel('Tipo de Evento')
plt.ylabel('Número de Eventos')
plt.xticks(rotation=0)  # Rótulos do eixo x agora estão horizontais
plt.show()

# Análise de gastos dos clientes
gastos = eventos_df.groupby('cliente')['valor'].sum()
sns.kdeplot(gastos)
plt.title('Distribuição de Gastos dos Clientes')
plt.xlabel('Valor Gasto')
plt.ylabel('Densidade entre os clientes')
plt.show()


print(eventos_df['id_oferta'].unique())
print(portfolio_df['id'].unique())  
print(merged_df['cliente'].unique())
print(clientes_df['id'].unique())
