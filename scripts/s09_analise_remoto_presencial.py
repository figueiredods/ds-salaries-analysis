 # Importar
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import config
import pandas as pd

# Carregar dataset
df = pd.read_csv(config.CSV_SALARIOS, index_col=0)

# Mapear remote_ratio para nomes descritivos
mapa_remote = {
    0: 'Presencial',
    50: 'Híbrido',
    100: 'Remoto'
}
mapa_experiencia = {
    'EN': 'Júnior (EN)',
    'MI': 'Pleno (MI)',
    'SE': 'Sênior (SE)',
    'EX': 'Executivo (EX)'
}

df['modelo_trabalho'] = df['remote_ratio'].map(mapa_remote)
df['nivel_experiencia'] = df['experience_level'].map(mapa_experiencia)

ordem_exp = ['Júnior (EN)', 'Pleno (MI)', 'Sênior (SE)', 'Executivo (EX)']
columas_modelo = ['Presencial', 'Híbrido', 'Remoto']

# Selecionar os 4 cargos com maior representativodade
top_4_cargos = df['job_title'].value_counts().head(4).index.tolist()

# Dicionário para armazenar as 4 tabelas geradas em loop
tabelas_por_cargo = {}

for cargo in top_4_cargos:
    df_cargo = df[df['job_title'] == cargo]

    tabela = df_cargo.pivot_table(
        index = 'nivel_experiencia',
        columns = 'modelo_trabalho',
        values = 'salary_in_usd',
        aggfunc = 'mean'
    ).reindex(ordem_exp)

    # Garantir que todas as colunas do modelo de trabalho existam na tabela
    for col in columas_modelo:
        if col not in tabela.columns:
            tabela[col] = float('nan')

    tabelas_por_cargo[cargo] = tabela[columas_modelo]

# Exibir no terminal as 4 tabelas
if __name__ == '__main__':
    print("\n" + "=" * 75)
    print("=== MÉDIA SALARIAL POR CARGO, EXPERIÊNCIA E MODELO DE TRABALHO (USD $) ===")
    print("=" * 75 + "\n")

    for cargo, tabela in tabelas_por_cargo.items():
        print(f"📌 CARGO: {cargo.upper()}")
        print("-" * 60)
        # Formatar print com $ sem alterar na tabela original
        tabela_formatada = tabela.map(lambda x: f'$ {x:,.2f}' if pd.notna(x) else '     -     ')
        print(tabela_formatada)
        print("\n" + "." * 75 + "\n")