# Imports
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

import pandas as pd
import config

# 1. Carregar o conjunto de dados
df = pd.read_csv(config.CSV_SALARIOS, index_col=0)

# 2. Visualizar as 5 primentas linhas
print(" --- PRIMEIRAS LINHAS --- ")
print(df.head())

# 3. Informações e Estatisticas
print("\n --- INFORMAÇÕES DO DATAFRAME --- ")
print(df.info())

print("\n --- ESTATÍSTICAS DO DATAFRAME --- ")
print(df['salary_in_usd'].describe().map(lambda x: f'$ {x:,.2f}'))

# 4. Quantidade de cargos diferentes no df
n_jobs_title = df["job_title"].nunique()

# 5. Lista de cargos diferentes e suas quantidades
jobs_title = df["job_title"].value_counts()

print(f"\n --- TOTAL DE CARGOS DIFERENTES: {n_jobs_title} --- ")

print(f"\n --- TOP 5 CARGOS (CONTAGEM POR CARGO) ---")
print(jobs_title.head())

# 6. Salário médio global em US$
salario_medio_global = df["salary_in_usd"].mean()

print(f"\n --- SALÁRIO MÉDIO GLOBAL (USD $): {salario_medio_global:,.2f} ---\n")

# 7. Maior e Menor salário e seus respectivos cargos
idx_max = df['salary_in_usd'].idxmax() # retorna o índice do maior valor na coluna 'salary_in_usd
idx_min = df['salary_in_usd'].idxmin()

maior_salario = df.loc[idx_max, 'salary_in_usd']
cargo_maior = df.loc[idx_max, 'job_title']

menor_salario = df.loc[idx_min, 'salary_in_usd']
cargo_menor = df.loc[idx_min, 'job_title']

print(f"\n --- MAIOR SALÁRIO (USD $): ${maior_salario:,.2f} ---")
print(f" --- CARGO: {cargo_maior} ---\n")

print(f"\n --- MENOR SALÁRIO (USD $): ${menor_salario:,.2f} ---")
print(f" --- CARGO: {cargo_menor} ---\n")