import pandas as pd
import matplotlib.pyplot as plt

# Carregar o conjunto de dados
df = pd.read_csv("/Users/danielfigueiredo/Library/CloudStorage/GoogleDrive-figueiredo.ds2018@gmail.com/My Drive/Documents/Portugal/estudo/python_java_sql_study/ds-salaries-analysis/dados/ds_salaries.csv", index_col=0)

# Agrupar pela hierarquida de carreira
ordem_carreira = ['EN', 'MI', 'SE', 'EX']
media_exp = df.groupby('experience_level')['salary_in_usd'].mean().reindex(ordem_carreira)

# Definir nomes explicativos e cores
niveis = ['EN (Junior)', 'MI (Pleno/Mid)', 'SE (Sénior)', 'EX (Executivo)']
salarios = media_exp.values
cores = ['#2b5c8f', '#3670a3', '#4682b4', '#1d3557']

# Criar a figura e os eixos (Canvas de Desenho)
fig, ax = plt.subplots(figsize = (9, 5.5))

# Desenhar as barras
barras = ax.bar(niveis, salarios, color = cores, width = 0.55)

# Adicionar os valores numéricos em cima de cada barra (Rótulos de Dados)
for barra in barras:
    altura = barra.get_height()
    ax.text(
        barra.get_x() + barra.get_width() / 2.0,
        altura + 3000,
        f"${altura:,.2f}",
        ha = 'center',
        va = 'bottom',
        fontsize = 10,
        fontweight = 'bold',
        color = '#1d3557'
    )

    # Personalizar títulos e rótulos dos eixos
    ax.set_title('Média Salarial por Nível de Experiência em Data Science', fontsize = 13, fontweight = 'bold', pad = 20, color = '#1d3557')
    ax.set_xlabel('Nível de Experiência', fontsize = 11, fontweight = 'bold', labelpad = 10)
    ax.set_ylabel('Salário Médio (USD)', fontsize = 11, fontweight = 'bold', labelpad = 10)

    # Ajustes de escala e formatação do Eixo Y
    ax.set_ylim(0, 230000)
    ax.yaxis.set_major_formatter('${x:,.0f}')
    ax.grid(axis = 'y', linestyle = '--', alpha = 0.5)
    ax.set_axisbelow(True)

    # Remover birdas desnecessárias (Design Limpo / Chartjunk)
    for borda in ['top', 'right', 'left']:
        ax.spines[borda].set_visible(False)

# Guardar a imagem na pasta do projeto e exibir
plt.tight_layout()
plt.savefig('/Users/danielfigueiredo/Library/CloudStorage/GoogleDrive-figueiredo.ds2018@gmail.com/My Drive/Documents/Portugal/estudo/python_java_sql_study/ds-salaries-analysis/imagens/grafico_salarios_experiencia.png', dpi = 300, bbox_inches = 'tight')
plt.show()

print("Gráfico 'imagens/grafico_salarios_experiencia.png' gerado com sucesso!")