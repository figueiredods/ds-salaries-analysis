# Importar
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent)) # ajuste para localozar o config na pasta raiz

import config
import matplotlib.pyplot as plt

from s07_analise_tamanho_empresa import df_resumo

# Praparar dados para o gráfico
rotulos = df_resumo.index
salarios = df_resumo['Salario_Medio'].values
cores = ['#2b5c8f', '#3670a3', '#4682b4']

# Construir o gráfico
fig, ax = plt.subplots(figsize = (8, 5.5))
barras = ax.bar(rotulos, salarios, color = cores, width = 0.5)

for barra in barras:
    altura = barra.get_height()
    ax.annotate(f'${altura:,.2f}',
                xy = (barra.get_x() + barra.get_width() / 2.0, altura),
                xytext = (0, 5),
                textcoords = 'offset points',
                ha = 'center', va = 'bottom',
                fontsize = 10, fontweight = 'bold', color = '#1d3557')

## Estilo do gráfico
ax.set_title('Média Salarial por Tamanho de Empresa', fontsize = 12, fontweight = 'bold', pad = 15, color = '#1d3557')
ax.set_xlabel('Tamanho da Empresa', fontsize = 11, fontweight = 'bold', labelpad = 10)
ax.set_ylabel('Salário Médio (USD $)', fontsize = 11, fontweight = 'bold', labelpad = 10)

## Ajuste do limite do eixo y
max_val = float(salarios.max())
ax.set_ylim(0, max_val * 1.18)
ax.yaxis.set_major_formatter('${x:,.0f}')
ax.grid(axis = 'y', linestyle = '--', alpha = 0.5)
ax.set_axisbelow(True)

## Remover bordas desnecessárias
for borda in ['top', 'right', 'left']:
    ax.spines[borda].set_visible(False)

# Salvar a imagem
plt.tight_layout()
plt.savefig(config.GRAFICO_TAMANHO_EMPRESA, dpi = 300, bbox_inches = 'tight')
plt.close()

print(f"\n✅ Gráfico salvo com sucesso em: {config.GRAFICO_TAMANHO_EMPRESA}\n")