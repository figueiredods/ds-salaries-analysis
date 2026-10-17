from pathlib import Path

# Diretorio raiz do projeto (Detecta automaticamente onde está o arquivo)
BASE_DIR = Path(__file__).resolve().parent

# Diretorios principais
DIR_DADOS = BASE_DIR / 'dados'
DIR_IMAGENS = BASE_DIR / 'imagens'
DIR_SCRIPTS =  BASE_DIR / 'scripts'

# Caminhos dos ficheiros de dados
CSV_SALARIOS = DIR_DADOS / 'ds_salaries.csv'
CSV_ISO = DIR_DADOS / 'iso_3166_data.csv'

# Caminhos dos gráficos gerados
GRAFICO_EXPERIENCIA = DIR_IMAGENS / 'grafico_salarios_experiencia.png'
GRAFICO_OFFSHORE = DIR_IMAGENS / 'grafico_salarios_offshore.png'
GRAFICO_PAISES = DIR_IMAGENS / 'grafico_salarios_paises.png'