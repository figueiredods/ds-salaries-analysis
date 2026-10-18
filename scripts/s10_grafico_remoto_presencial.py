# Importar
import sys 
from pathlib import Path 
sys.path.append(str(Path(__file__).resolve().parent.parent)) 
import config 
import matplotlib.pyplot as plt 
import numpy as np 

# Importação das 4 tabelas geradas no script 09
from scripts.s09_analise_remoto_presencial import tabelas_por_cargo, ordem_exp 

# Configuração da figura com grade 2x2 
fig, axes = plt.subplots(2, 2, figsize=(14, 10), sharey=True) 
axes_achatados = axes.flatten() 

# Rótulos simplificados para o eixo X 
rotulos_x = ['Júnior', 'Pleno', 'Sênior', 'Executivo'] 
x = np.arange(len(rotulos_x)) 
largura = 0.25 

cores = {'Presencial': '#2b5c8f', 'Híbrido': '#e67e22', 'Remoto': '#2ca02c'} 

# Loop para desenhar cada um dos 4 cargos num quadrante 
for i, (cargo, tabela) in enumerate(tabelas_por_cargo.items()):
    ax = axes_achatados[i] 
    
    # Deslocamento das barras para Presencial, Híbrido e Remoto
    ax.bar(x - largura, tabela['Presencial'], largura, label='Presencial', color=cores['Presencial']) 
    ax.bar(x, tabela['Híbrido'], largura, label='Híbrido', color=cores['Híbrido']) 
    ax.bar(x + largura, tabela['Remoto'], largura, label='Remoto', color=cores['Remoto']) 
    
    # Estilização individual do quadrante 
    ax.set_title(cargo, fontsize=12, fontweight='bold', color='#1d3557', pad=10) 
    ax.set_xticks(x) 
    ax.set_xticklabels(rotulos_x, fontsize=9, fontweight='bold') 
    ax.yaxis.set_major_formatter('${x:,.0f}') 
    ax.grid(axis='y', linestyle='--', alpha=0.5) 
    ax.set_axisbelow(True) 
    
    for borda in ['top', 'right', 'left']:
        ax.spines[borda].set_visible(False) 

# Legenda única no topo da figura 
handles, labels = axes_achatados[0].get_legend_handles_labels() 
fig.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5, 0.98), ncol=3, fontsize=11, frameon=False) 

# Título Geral 
fig.suptitle('Média Salarial por Cargo, Experiência e Modelo de Trabalho', fontsize=15, fontweight='bold', color='#1d3557', y=1.02) 

# Salvar a imagem 
plt.tight_layout() 
plt.savefig(config.GRAFICO_REMOTO, dpi=300, bbox_inches='tight') 
plt.close() 
print(f"\n✅ Gráfico do painel 2x2 salvo com sucesso em: {config.GRAFICO_REMOTO}\n")