# imports
import sys
from pathlib import Path

#Ajuste de caminho para localizar o config.py na pasta raiz do projeto
sys.path.append(str(Path(__file__).resolve().parent.parent))

import pandas as pd
import config

# Carregar o Dataset
df = pd.read_csv(config.CSV_SALARIOS, index_col=0)

# NOTA DE MANUTENÇÃO: Usamos 'keep_default_na=False' para impedir que o Pandas interprete a sigla 'NA' (Namíbia) como valor nulo (NaN).
df_iso = pd.read_csv(config.CSV_ISO, keep_default_na = False) # keep_default_na = False faz com que o pandas não considere a sigla NA como um campo vazio

# VALIDAÇÃO DE INTEGRIDADE - Garantir que nenhuma sigla de país ficou vazia antes de prosseguir
assert df_iso['Code'].isna().sum() == 0, "Erro: Existem códigos ISO nulos na tabela de países!"

# Mapeamento dos nomes dos países 
df_iso = df_iso.set_index('Code')
df['pais_residencia'] = df['employee_residence'].map(df_iso['Name']) 
df['pais_empresa'] = df['company_location'].map(df_iso['Name'])

# criar a coluna Offshore (país residencia != país companhia)
df["offshore"] = df['employee_residence'] != df['company_location']

# --PROCESSAMENTO 1: EMPRESAS DOS EUA (LOCAL VS OFFSHORE)
df_us = df[df['company_location'] == 'US']
df_us_agrupado = df_us.groupby('offshore')['salary_in_usd'].mean()

nomes_booleanos = {
    False: 'USA',
    True: 'Offshore'
}

df_resumo = pd.DataFrame({
    'Salario_Medio': df_us_agrupado,
    'Diferenca_Absoluta': df_us_agrupado.diff(periods = -1),
    'Variacao_Percentual': df_us_agrupado.pct_change(periods = -1) * 100
})

# --PROCESSAMENTO 2: EMPRESAS DOS EUA (LOCAL VS OFFSHORE)
df_paises_filtrado = df.groupby('pais_residencia')['salary_in_usd'].agg(['count', 'mean', 'median']).query('count >= 5').sort_values(by = 'mean', ascending = False)

# --- EXIBIÇÃO NO TERMINAL (Executa apenas ao rodar este arquivo diretamente) ---
if __name__ == '__main__':
    print("\n" + "~" * 65)
    print("=== ANÁLISE DE TRABALHO OFFSHORE EM EMPRESAS EUA ===")
    print("~" * 65)
    print(f"{'Localização':<20} | {'Salário Médio':<15} | {'Diferença':<25}") # <20 é a formatação de alinhamento à esquerda
    print("~" * 65)

    # percorrer e formatar exibição
    for local, linha in df_resumo.iterrows():
        nome_exibicao = nomes_booleanos[local]
        salario_formatado = f"${linha['Salario_Medio']:>11,.2f}"

        if pd.isna(linha['Diferenca_Absoluta']):
            aumento_str = "-"
        else:
            abs_val = f"+$ {linha['Diferenca_Absoluta']:,.2f}"
            pct_val = f"(+ {linha['Variacao_Percentual']:.1f}%)"
            aumento_str = f"{abs_val} {pct_val}"
        print(f"{nome_exibicao:<20} | {salario_formatado:<15} | {aumento_str:<25}")

    print("~" * 65 + "\n")

    print("=== SALÁRIO MÉDIO/MEDIANO POR PAÍS DE RESIDÊNCIA (COUNT >= 5) ===")
    print(df_paises_filtrado.map(lambda x: f'$ {x:,.2f}'))