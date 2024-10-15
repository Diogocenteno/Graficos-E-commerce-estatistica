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

    # Criando o histograma
    sns.histplot(df['Nota'], bins=20, kde=True, color='skyblue', alpha=0.7)

    # Calculando média e mediana
    media = df['Nota'].mean()
    mediana = df['Nota'].median()

    # Adicionando linhas verticais para média e mediana
    plt.axvline(media, color='red', linestyle='--', label=f'Média: {media:.2f}')
    plt.axvline(mediana, color='green', linestyle='--', label=f'Mediana: {mediana:.2f}')

    plt.title('Distribuição da Nota dos Produtos')
    plt.xlabel('Nota')
    plt.ylabel('Frequência')
    plt.xticks(rotation=45)
    plt.grid(axis='y')

    # Adicionando a legenda
    plt.legend(loc='upper right')

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
    plt.figure(figsize=(14, 8))  # Aumentando o tamanho da figura

    # Calculando a média da nota por marca e filtrando as 10 principais
    top_brands = df.groupby('Marca')['Nota'].mean().nlargest(10).reset_index()

    # Criando o gráfico de barra
    barplot = sns.barplot(data=top_brands, x='Marca', y='Nota', palette='viridis', legend=False)

    plt.title('Média da Nota por Marca (Top 10)', fontsize=18, fontweight='bold')
    plt.xlabel('Marca', fontsize=14)
    plt.ylabel('Nota Média', fontsize=14)
    plt.xticks(rotation=45, fontsize=12)
    plt.yticks(fontsize=12)

    # Adicionando as anotações de valor
    for p in barplot.patches:
        barplot.annotate(f'{p.get_height():.2f}',
                         (p.get_x() + p.get_width() / 2., p.get_height()),
                         ha='center', va='bottom',
                         color='black', fontsize=12)

    plt.grid(axis='y', linestyle='--', alpha=0.7)  # Linhas de grade mais suaves

    # Adicionando uma legenda à direita do gráfico
    plt.legend(['Nota Média'], loc='upper right', bbox_to_anchor=(1.25, 1), fontsize=12)

    plt.tight_layout()  # Ajusta o layout para evitar sobreposições
    plt.savefig('grafico_barra_nota_por_marca_top10.png', dpi=300)  # Salvando o gráfico com alta resolução
    plt.show()  # Exibe o gráfico

# Função para Gráfico de Pizza
def plot_grafico_pizza():
    plt.figure(figsize=(8, 8))

    # Contagem de Gêneros
    genero_counts = df['Gênero'].value_counts()

    # Calculando as porcentagens
    porcentagens = 100 * genero_counts / genero_counts.sum()

    # Criando gráfico de pizza sem porcentagens visíveis
    wedges, texts = plt.pie(genero_counts,
                            startangle=90,
                            colors=sns.color_palette('pastel'),
                            wedgeprops=dict(edgecolor='white'))

    # Adicionando um círculo no centro para criar um gráfico de rosca
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)

    plt.title('Distribuição de Gênero dos Produtos', fontsize=16)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Criando a legenda com porcentagens
    legenda_textos = [f'{gênero}: {porcentagem:.1f}%' for gênero, porcentagem in zip(genero_counts.index, porcentagens)]
    plt.legend(legenda_textos, title='Gênero', loc='upper right', bbox_to_anchor=(1.3, 1))

    plt.savefig('grafico_pizza_genero.png')  # Salvando o gráfico
    plt.show()  # Exibe o gráfico

# Função para Gráfico de Densidade
def plot_grafico_densidade():
    plt.figure(figsize=(10, 6))
    sns.kdeplot(df['Preço'], fill=True, color='blue', alpha=0.5)

    plt.title('Densidade da Distribuição de Preço')
    plt.xlabel('Preço')
    plt.ylabel('Densidade')

    # Adicionando anotações com estatísticas
    media = df['Preço'].mean()
    mediana = df['Preço'].median()
    plt.axvline(media, color='red', linestyle='--', label=f'Média: {media:.2f}')
    plt.axvline(mediana, color='green', linestyle='--', label=f'Mediana: {mediana:.2f}')

    plt.legend(loc='upper right')
    plt.grid()
    plt.savefig('grafico_densidade_preco.png')  # Salvando o gráfico
    plt.show()  # Exibe o gráfico

# Função para Gráfico de Regressão
def plot_grafico_regressao():
    plt.figure(figsize=(10, 6))
    sns.regplot(data=df, x='Preço', y='Nota', scatter_kws={'alpha': 0.5}, line_kws={'color': 'red'})

    plt.title('Regressão entre Preço e Nota')
    plt.xlabel('Preço')
    plt.ylabel('Nota')

    # Adicionando anotações com estatísticas
    r_squared = sns.regplot(data=df, x='Preço', y='Nota').get_lines()[0].get_xydata()[0][1]
    plt.text(0.05, 0.95, f'$R^2$: {r_squared:.2f}', fontsize=12, transform=plt.gca().transAxes, verticalalignment='top')

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
