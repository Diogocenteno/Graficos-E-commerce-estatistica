import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Lendo o arquivo CSV em um DataFrame
df = pd.read_csv('C:/Users/diogo/Desktop/ecommerce_estatistica.csv')

# Exibindo as primeiras linhas do DataFrame
print(df.head())

# Exibir informações gerais do DataFrame
print(df.info())

# Exibir estatísticas descritivas
print(df.describe())

# Definindo a opção para exibir todas as colunas
pd.set_option('display.max_columns', None)

# Exibindo o DataFrame
print(df)

# Verificando dados ausentes
print(df.isnull().sum())

# Função para Gráfico de Histograma
def plot_histograma():
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Nota'], bins=20, kde=True)
    plt.title('Distribuição da Nota dos Produtos')
    plt.xlabel('Nota')
    plt.ylabel('Frequência')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.savefig('histograma_nota.png')  # Salvando o gráfico
    plt.show()  # Exibe o gráfico

# Função para Gráfico de Dispersão
def plot_dispercao():
    plt.figure(figsize=(10, 6))
    scatter = plt.scatter(data=df, x='Preço', y='Qtd_Vendidos', c=df['Nota'], cmap='viridis', alpha=0.7)
    plt.title('Relação entre Preço e Quantidade Vendida')
    plt.xlabel('Preço')
    plt.ylabel('Quantidade Vendida')
    plt.xticks(rotation=45)
    plt.grid()
    plt.colorbar(scatter, label='Nota')  # Adiciona uma barra de cores
    plt.savefig('dispersao_preco_qtd_vendidos.png')  # Salvando o gráfico
    plt.show()  # Exibe o gráfico

# Função para Mapa de Calor
def plot_mapa_calor():
    plt.figure(figsize=(12, 8))
    numeric_df = df.select_dtypes(include=[np.number])
    correlation_matrix = numeric_df.corr()
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True)
    plt.title('Mapa de Calor da Correlação entre Variáveis')
    plt.xticks(rotation=45)
    plt.yticks(rotation=45)
    plt.savefig('mapa_calor_correlacao.png')  # Salvando o gráfico
    plt.show()  # Exibe o gráfico

# Função para Gráfico de Barra
def plot_grafico_barra():
    plt.figure(figsize=(12, 6))

    # Calculando a média da nota por marca e filtrando as 10 principais
    top_brands = df.groupby('Marca')['Nota'].mean().nlargest(10).reset_index()

    # Criando o gráfico de barra com hue
    sns.barplot(data=top_brands, x='Marca', y='Nota', hue='Marca', dodge=False, palette='viridis', legend=False)
    plt.title('Média da Nota por Marca (Top 10)')
    plt.xlabel('Marca')
    plt.ylabel('Nota Média')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.savefig('grafico_barra_nota_por_marca_top10.png')  # Salvando o gráfico
    plt.show()  # Exibe o gráfico

# Função para Gráfico de Pizza
def plot_grafico_pizza():
    plt.figure(figsize=(8, 8))

    # Contagem de Gêneros
    genero_counts = df['Gênero'].value_counts()

    # Criando gráfico de rosca
    wedges, texts, autotexts = plt.pie(genero_counts,
                                       autopct='%1.1f%%',
                                       startangle=90,
                                       colors=sns.color_palette('pastel'),
                                       wedgeprops=dict(edgecolor='white'))

    # Configurações de estilo
    plt.setp(autotexts, size=12, weight="bold", color="white")
    plt.setp(texts, size=14, weight="bold")

    # Adicionando um círculo no centro para criar um gráfico de rosca
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)

    plt.title('Distribuição de Gênero dos Produtos', fontsize=16)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.legend(genero_counts.index, title='Gênero', loc='upper right', bbox_to_anchor=(1.2, 1))

    plt.savefig('grafico_pizza_genero_melhorado.png')  # Salvando o gráfico
    plt.show()  # Exibe o gráfico

# Função para Gráfico de Densidade
def plot_grafico_densidade():
    plt.figure(figsize=(10, 6))
    sns.kdeplot(df['Preço'], fill=True)
    plt.title('Densidade da Distribuição de Preço')
    plt.xlabel('Preço')
    plt.ylabel('Densidade')
    plt.grid()
    plt.savefig('grafico_densidade_preco.png')  # Salvando o gráfico
    plt.show()  # Exibe o gráfico

# Função para Gráfico de Regressão
def plot_grafico_regressao():
    plt.figure(figsize=(10, 6))
    sns.regplot(data=df, x='Preço', y='Nota', scatter_kws={'alpha': 0.5})
    plt.title('Regressão entre Preço e Nota')
    plt.xlabel('Preço')
    plt.ylabel('Nota')
    plt.grid()
    plt.savefig('grafico_regressao_preco_nota.png')  # Salvando o gráfico
    plt.show()  # Exibe o gráfico

# Chame as funções que deseja exibir
plot_histograma()
plot_dispercao()
plot_mapa_calor()
plot_grafico_barra()
plot_grafico_pizza()
plot_grafico_densidade()
plot_grafico_regressao()
