# Imports
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import config
import matplotlib.pyplot as plt

# Importar dados já calculados no arquivo s02_analise_salario_exp
from s02_analise_salario_exp import df_resumo, nomes_niveis

# Definir nomes explicativos e cores
rotulos = [nomes_niveis[nivel] for nivel in df_resumo.index]
valores = df_resumo['Salario_Medio']

# Criar a figura
fig, ax = plt.subplots(figsize = (8, 5))
ax.bar(rotulos, valores, color = '#2b5c8f')

ax.set_title('Salário Médio por Nível de Experiência', fontsize = 12, fontweight = 'bold') # título
ax.set_ylabel('Salário Anual (USD $)', fontsize = 10) # eixo y
ax.yaxis.set_major_formatter('$ {x:,.0f}')
ax.grid(axis = 'y', linestyle = '--', alpha = 0.5)

# Guardar a imagem na pasta do projeto e exibir
plt.tight_layout()
plt.savefig(config.GRAFICO_EXPERIENCIA, dpi = 300, bbox_inches = 'tight')
plt.close()

print(f"\n✅ Gráfico de Experiência salvo em: {config.GRAFICO_EXPERIENCIA}\n")