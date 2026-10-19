# Imports
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import config
import matplotlib.pyplot as plt

# importando os dados já filtrados e processados do script 04
from scripts.s04_analise_geografica import df_us_agrupado

# Definir rótulos, valores e cores
booleanos = ['USA (Local)', 'Offshore (Remoto)']
salarios = df_us_agrupado.values
cores = ['#2b5c8f', '#3670a3']

# Criar a figura
fig, ax = plt.subplots(figsize = (8, 5.5))

# Configurar barras
barras = ax.bar(booleanos, salarios, color = cores, width = 0.45)

# Adicionar os valores acima das barras
for barra in barras:
    altura = barra.get_height()
    ax.annotate(f'${altura:,.2f}',
        xy = (barra.get_x() + barra.get_height() / 2.0, altura),
        xytext = (0, 5),
        textcoords = 'offset points',
        ha = 'center', va = 'bottom', fontsize = 10, fontweight = 'bold', color = '#1d3557')

    # Estilo
    ax.set_title('Média Salarial em Empresas dos EUA: Local vs. Offshore', fontsize = 12, fontweight = 'bold', pad = 15, color = '#1d3557')
    ax.set_xlabel('Localização do Trabalhador', fontsize = 11, fontweight = 'bold', labelpad = 10)
    ax.set_ylabel('Salário Médio (USD $)', fontsize = 11, fontweight = 'bold', labelpad = 10)

    ax.set_ylim(0, max(salarios) * 1.18)
    ax.yaxis.set_major_formatter('${x:,.0f}')
    ax.grid(axis = 'y', linestyle = '--', alpha = 0.5)
    ax.set_axisbelow(True)

    # Remover bordas deesnecessárias
    for borda in ['top', 'right', 'left']:
        ax.spines[borda].set_visible(False)

# Guardar a imagem na parta do projeto e exibir
plt.tight_layout()
plt.savefig(config.GRAFICO_OFFSHORE, dpi = 300, bbox_inches = 'tight')
plt.close()

print(f"\n✅ Gráfico salvo com sucesso em: {config.GRAFICO_OFFSHORE}\n")