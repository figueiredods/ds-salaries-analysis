# Importar bibliotecas
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import os
import pandas as pd
import config

# Carregar dados
df = pd.read_csv(config.CSV_SALARIOS, index_col = 0)

# Mapear códigos de tamanho
mapa_tamanho = {
    'S': 'Pequena (<50)',
    'M': 'Média (50 - 250)',
    'L': 'Grande (>250)'
}

# Organizar por ordem de tamanho
ordem_tamanho = ['Pequena (<50)', 'Média (50 - 250)', 'Grande (>250)']

df['tamanho_empresa'] = df['company_size'].map(mapa_tamanho)

# Agrupar por tamanho e calcular as métricas
df_agrupado_tamanho_empresa = df.groupby('tamanho_empresa')['salary_in_usd'].mean().reindex(ordem_tamanho)

df_resumo = pd.DataFrame({
    'Salario_Medio': df_agrupado_tamanho_empresa,
    'Diferenca_Absoluta': df_agrupado_tamanho_empresa.diff(periods = 1),
    'Variacao_Percentual': df_agrupado_tamanho_empresa.pct_change(periods = 1) * 100
})

if __name__ == '__main__':
    print("\n" + "~" * 65)
    print("=== ANÁLISE DE SALÁRIO MÉDIO POR TAMANHO DE EMPRESA ===")
    print("~" * 65)
    print(f"{'Tamanho':<20} | {'Salário Médio':<15} | {'Diferença':<25}") # <20 é a formatação de alinhamento à esquerda
    print("~" * 65)

    # percorrer e formatar exibição
    for local, linha in df_resumo.iterrows():
        nome_exibicao = local
        salario_formatado = f"${linha['Salario_Medio']:>11,.2f}"

        if pd.isna(linha['Diferenca_Absoluta']):
            aumento_str = "-"
        else:
            abs_val = f"+$ {linha['Diferenca_Absoluta']:,.2f}"
            pct_val = f"(+ {linha['Variacao_Percentual']:.1f}%)"
            aumento_str = f"{abs_val} {pct_val}"
        print(f"{nome_exibicao:<20} | {salario_formatado:<15} | {aumento_str:<25}")

    print("~" * 65 + "\n")