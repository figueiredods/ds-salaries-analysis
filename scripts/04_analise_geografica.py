# imports
import os
import pandas as pd
import matplotlib.pyplot as plt

# Variáveis de caminho absoluto dos arquivos e pastas

caminho_csv = '/Users/danielfigueiredo/Library/CloudStorage/GoogleDrive-figueiredo.ds2018@gmail.com/My Drive/Documents/Portugal/estudo/python_java_sql_study/ds-salaries-analysis/dados/ds_salaries.csv'

pasta_imagens = '/Users/danielfigueiredo/Library/CloudStorage/GoogleDrive-figueiredo.ds2018@gmail.com/My Drive/Documents/Portugal/estudo/python_java_sql_study/ds-salaries-analysis/imagens'

caminho_grafico = '/Users/danielfigueiredo/Library/CloudStorage/GoogleDrive-figueiredo.ds2018@gmail.com/My Drive/Documents/Portugal/estudo/python_java_sql_study/ds-salaries-analysis/imagens/grafico_salarios_offshore.png'

# Garantir que a pasta existe
os.makedirs(pasta_imagens, exist_ok = True)

# Carregar o Dataset
df = pd.read_csv(caminho_csv, index_col=0)

# criar a coluna Offshore (país residencia != país companhia)
df["offshore"] = df['employee_residence'] != df['company_location']

print(df[['employee_residence', 'company_location', 'offshore']].head())

# Criar novo DF apenas com empresas USA
df_us = df[df['company_location'] == 'US']

# Agrupar por offshore
df_us_agrupado = df_us.groupby('offshore')['salary_in_usd'].mean()

# Renomeando os booleanos
nomes_booleanos = {
    False: 'USA',
    True: 'Offshore'
}

# DataFrame resuma
df_resumo = pd.DataFrame({
    'Salario_Medio': df_us_agrupado,
    'Diferenca_Absoluta': df_us_agrupado.diff(periods = -1),
    'Variacao_Percentual': df_us_agrupado.pct_change(periods = -1) * 100
})

# Tabela
print("\n" + "~" * 60)
print(f"{'Localização':<15} | {'Salário Médio':<15} | {'Diferença':<25}") # <20 é a formatação de alinhamento à esquerda
print("~" * 60)

# percorrer e formatar exibição
for local, linha in df_resumo.iterrows():
    nome_exibicao = nomes_booleanos[local]
    salario_formatado = f"${linha['Salario_Medio']:>10,.2f}"

    if pd.isna(linha['Diferenca_Absoluta']):
        aumento_str = "-"
    else:
        abs_val = f"+${linha['Diferenca_Absoluta']:,.2f}"
        pct_val = f"(+{linha['Variacao_Percentual']:.1f}%)"
        aumento_str = f"{abs_val} {pct_val}"
    print(f"{nome_exibicao:<15} | {salario_formatado:<15} | {aumento_str:<25}")

print("~" * 60 + "\n")