# Imports
import pandas as pd

# 1. Carregar o conjunto de dados
df = pd.read_csv("dados/ds_salaries.csv", index_col=0)
# df = pd.read_csv("dados/ds_salaries.csv", usecols = lambda x: x != "Unnamed: 0") - alternativa para remover coluna quando lê o arquivo

# 2. Visualizar as 5 primentas linhas
print(" --- PRIMEIRAS LINHAS --- ")
print(df.head())

# 3. Vverificar informações das colunas e tipos de dados
print("\n --- INFORMAÇÕES DO DATAFRAME --- ")
print(df.info())

# 4. Quantidade de cargos diferentes no df
n_jobs_title = df["job_title"].nunique()

# 5. Lista de cargos diferentes e suas quantidades
jobs_title = df["job_title"].value_counts()

print("\n --- TOTAL DE CARGOS DIFERENTES --- ")
print(f"Existem neste DataSet um total de {n_jobs_title} diferentes tipos de cargos.")

print("\n --- TOP 5 CARGOS --- ")
print(jobs_title.head())

# 6. Salário médio global em US$
salario_medio_global = df["salary_in_usd"].mean()

print("\n --- SALÁRIO MÉDIO GLOBAL EM US$ --- ")
print(f"Salário médio global: ${salario_medio_global:,.2f}")