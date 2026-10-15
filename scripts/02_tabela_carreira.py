import pandas as pd

# 1. Carregar o conjunto de dados
caminho_csv = '/Users/danielfigueiredo/Library/CloudStorage/GoogleDrive-figueiredo.ds2018@gmail.com/My Drive/Documents/Portugal/estudo/python_java_sql_study/ds-salaries-analysis/dados/ds_salaries.csv'

df = pd.read_csv(caminho_csv, index_col=0)

# 2. Agrupar por nível
ordem_carreira = ["EN", "MI", "SE", "EX"]
media_salario_exp = df.groupby("experience_level")["salary_in_usd"].mean().reindex(ordem_carreira)

# 3. Criar um DataFrame de resumo com diferença e variação percentual
df_resumo = pd.DataFrame({
    'Salario_Medio': media_salario_exp,
    'Aumento_Absoluto': media_salario_exp.diff(), # subtrai o valor atual do valor presente na linha anteior
    'Aumento_Percentual': media_salario_exp.pct_change() * 100 # calcula a variação entre a linha atual e a linha anterior
})

# 4. Mapear os nomes explicativos para exibição
nomes_niveis = {
    'EN': 'EN (Junior)',
    'MI': 'MI (Pleno/Mid)',
    'SE': 'SE (Sénior)',
    'EX': 'EX (Executivo)'
}

# 5. Impressão da tabela formatada
print("\n" + "=" * 70)
print(f"{'Nivel de Experiência':<20} | {'Salário Médio':<15} | {'Aummento vs Nível Anterior':<25}") # <20 é a formatação de alinhamento à esquerda
print("=" * 70)

# Percorrer cada linha e formatar a exibição
for nivel, linha in df_resumo.iterrows():
    nome_exibicao = nomes_niveis[nivel]
    salario_formatado = f"${linha['Salario_Medio']:>10,.2f}" # >10 formatação de alinhamento à direita

    # Se for o nível Junior (primeira linna), não existe o nível anterior
    if pd.isna(linha["Aumento_Absoluto"]): # verifica se a linha, na coluna indicada, possui valorer NaN
        aumento_str = "-"
    else:
        abs_val = f"+${linha['Aumento_Absoluto']:,.2f}"
        pct_val = f"(+{linha['Aumento_Percentual']:.1f}%)"
        aumento_str = f"{abs_val}  {pct_val}"

    # Imprime a linha formatada com a largura fixa de colunas
    print(f"{nome_exibicao:<20} | {salario_formatado:<15} | {aumento_str:<25}")

print("-" * 70 + "\n")

# Montando o gráfico
fig, ax = plt.subplots