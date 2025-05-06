# -*- coding: utf-8 -*-

"""
Análise de Correspondência Múltipla - MCA

Dados: https://www.kaggle.com/datasets/jayaantanaath/student-habits-vs-academic-performance


"""
#%% Carregar as bibliotecas

# Executar o seguinte comando no console: pip install -r requirements.txt

# Em seguida, importar os pacotes

import pandas as pd
import prince
import itertools
from scipy.stats import chi2_contingency



#%% 

# Importar o banco de dados

perfil_mca = pd.read_csv("student_habits_performance.csv")

print(perfil_mca)



#%% Selecionando apenas variável categoricas

perfil_mca_select = perfil_mca.drop(columns=perfil_mca.select_dtypes(include='number').columns)

perfil_mca_select = perfil_mca_select.drop(columns=['student_id'])

print(perfil_mca_select)

#%% Analisando as tabelas de contingência

# Lista das colunas categóricas
colunas_categoricas = perfil_mca_select.select_dtypes(include=['object', 'category']).columns.tolist()

# Gerador de pares únicos de colunas (combinations sem repetição)
pares_colunas = list(itertools.combinations(colunas_categoricas, 2))

# Dicionário para armazenar as tabelas com nomes como 'tabela_mca_1', etc.
tabelas_contingencia = {}

# Criando as tabelas
for i, (col1, col2) in enumerate(pares_colunas, start=1):
    nome_tabela = f"tabela_mca_{i}"
    tabelas_contingencia[nome_tabela] = pd.crosstab(perfil_mca_select[col1], perfil_mca_select[col2])
    print(f"{nome_tabela} = pd.crosstab(perfil_mca_select[\"{col1}\"], perfil_mca_select[\"{col2}\"])\n")

# Agora você pode acessar, por exemplo: tabelas_contingencia["tabela_mca_1"]

# imprime todas as tabelas de contingencia
for nome, tabela in tabelas_contingencia.items():
    print(f"\n{nome}:\n")
    print(tabela)


#%% Analisando a significância estatística das associações (teste qui²)
## se P-valor < 0,05 descartamos H0, ou sejam há associação significativa

for i, (nome, tabela) in enumerate(tabelas_contingencia.items(), start=1):
    chi2, pvalor, df, freq_esp = chi2_contingency(tabela)

    print(f"Associação {i}")
    print(f"estatística qui²: {chi2}")
    print(f"p-valor da estatística: {pvalor}")
    print(f"graus de liberdade: {df} \n")


#%% Elaborando a MCA 

## Utiliza o método da matriz de Burt

mca = prince.MCA()
mca = mca.fit(perfil_mca_select)
# observe que com o fit não é necessário fazer a matriz de burt ou a matriz de correspondencias
#%% Obtendo as coordenadas nas duas dimensões do mapa

print(mca.column_coordinates(perfil_mca_select))

#%% Obtendo as coordenadas de cada um das observações

print(mca.row_coordinates(perfil_mca_select))

#%% Obtendo os eigenvalues

print(mca.eigenvalues_)

#%% Inércia principal total

print(mca.total_inertia_)

#%% Obtendo a variância

print(mca.explained_inertia_)

#%% Plotando o mapa 


mp_mca = mca.plot_coordinates(
             X = perfil_mca_select,
             figsize=(12,9),
             show_row_points = False, #False limpa o gráfico
             show_column_points = True,
             show_row_labels=False,
             column_points_size = 100,
             show_column_labels = True,
             legend_n_cols = 2)
mp_mca.set_title("Mapa de Correspondência - Perfil MCA", fontsize=16)


#%% Plotando o mapa perceptual interativo

import plotly.graph_objects as go
import plotly.io as pio

pio.renderers.default='browser'

chart_df = pd.DataFrame({'obs_x':mca.row_coordinates(perfil_mca_select)[0],
                         'estudante':perfil['Estudante'],
                         'obs_y': mca.row_coordinates(perfil_mca_select)[1]})

fig = go.Figure(data=go.Scatter(x=chart_df['obs_x'],
                                y=chart_df['obs_y'],
                                mode='markers',
                                name="Estudante",
                                text=chart_df['estudante']))

fig.add_trace(go.Scatter(
    x=mca.column_coordinates(perfil_mca_select)[0],
    mode='markers+text',
    name="Associação",
    marker={'size':12},
    y=mca.column_coordinates(perfil_mca_select)[1],
    textposition="top center",
    text=mca.column_coordinates(perfil_mca_select).index
))

fig.update_layout(
    autosize=False,
    width=800,
    height=800,
    title_text='Coordenadas das linhas e colunas'
)

fig.show()

