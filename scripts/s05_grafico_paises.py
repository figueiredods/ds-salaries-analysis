# Imports
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import config
import matplotlib.pyplot as plt

# importando os dados já filtrados e processados do script 04
from scripts.s04_analise_geografica import df_paises_filtrado

# Ordenar do menor para o maior para exibição em gráfico horizontal
df_medias = df_paises_filtrado.sort_values(by = 'mean', ascending = True)

# Criar a figura
fig, ax = plt.subplots(figsize = (10, 6))

# Configurar barras
barras = ax.barh(df_medias.index, df_medias['mean'], color = '#2b5c8f', height = 0.6)

# Rótulos de valor no final de cada barra
for barra in barras:
    largura = barra.get_height()
    ax.annotate(f'${largura:,.0f}',
        xy = (largura, barra.get_y() + barra.get_height() / 2),
        xytext = (6, 0),
        textcoords = 'offset points',
        ha = 'left', va = 'center', fontsize = 9, fontweight = 'bold', color = '#1d3557')

    # Estilo
    ax.set_title('Média Salarial por País de Residência (Amostra ≥ 5)', fontsize = 13, fontweight = 'bold', pad = 15, color = '#1d3557')
    ax.set_xlabel('Média Salarial Anual (USD $)', fontsize = 11, fontweight = 'bold', labelpad = 10)
    ax.set_ylabel('País de Residência', fontsize = 11, fontweight = 'bold', labelpad = 10)

    ax.set_xlim(0, df_medias['mean'].max() * 1.15)
    ax.xaxis.set_major_formatter('${x:,.0f}')
    ax.grid(axis = 'x', linestyle = '--', alpha = 0.5)
    ax.set_axisbelow(True)

    # Remover bordas deesnecessárias
    for borda in ['top', 'right']:
        ax.spines[borda].set_visible(False)

# Guardar a imagem na parta do projeto e exibir
plt.tight_layout()
plt.savefig(config.GRAFICO_PAISES, dpi = 300, bbox_inches = 'tight')
plt.close()

print(f"\n✅ Gráfico salvo com sucesso em: {config.GRAFICO_PAISES}\n")