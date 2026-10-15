import pandas as pd
import matplotlib.pyplot as plt

# Variável caminho
caminho_csv = '/Users/danielfigueiredo/Library/CloudStorage/GoogleDrive-figueiredo.ds2018@gmail.com/My Drive/Documents/Portugal/estudo/python_java_sql_study/ds-salaries-analysis/dados/ds_salaries.csv'

caminho_grafico = '/Users/danielfigueiredo/Library/CloudStorage/GoogleDrive-figueiredo.ds2018@gmail.com/My Drive/Documents/Portugal/estudo/python_java_sql_study/ds-salaries-analysis/imagens/grafico_salarios_offshore.png'

# Carregamento DataSet
df = pd.read_csv(caminho_csv, index_col = 0)

# criar a coluna Offshore (país residencia != país companhia)
df["offshore"] = df['employee_residence'] != df['company_location']

print(df[['employee_residence', 'company_location', 'offshore']].head())

# Criar novo DF apenas com empresas USA
df_us = df[df['company_location'] == 'US']

# Agrupar por offshore
df_us_agrupado = df_us.groupby('offshore')['salary_in_usd'].mean()

# Definir nomes explicativos
booleanos = ['USA', 'Offshore']
salarios = df_us_agrupado.values
cores = ['#2b5c8f', '#3670a3', '#4682b4', '#1d3557']

# Criar a figura e os eixos
fig, ax = plt.subplots(figsize = (9, 5.5))

# Configurar barras
barras = ax.bar(booleanos, salarios, color = cores, width = 0.55)

# Adicionar os valores para as barras
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

    # Personalizar títulos e rótulos
    ax.set_title('Média Salarial por Localização', fontsize = 13, fontweight = 'bold', pad = 20, color = '#1d3557')
    ax.set_xlabel('Localização', fontsize = 11, fontweight = 'bold', labelpad = 10)
    ax.set_ylabel('Salário Médio (USD)', fontsize = 11, fontweight = 'bold', labelpad = 10)

    # Ajuste de escala e formatação eixo Y
    ax.set_ylim(0, 230000)
    ax.yaxis.set_major_formatter('${x:,.0f}')
    ax.grid(axis = 'y', linestyle = '--', alpha = 0.5)
    ax.set_axisbelow(True)

    # Remover bordas deesnecessárias
    for borda in ['top', 'right', 'left']:
        ax.spines[borda].set_visible(False)

# Guardar a imagem na parta do projeto e exibir
plt.tight_layout()
plt.savefig(caminho_grafico, dpi = 300, bbox_inches = 'tight')
plt.show()

print("Gráfico 'imagens/grafico_salarios_offshore.png' gerado com sucesso!")