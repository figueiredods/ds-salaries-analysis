from pathlib import Path

# Project root directory (automatically detects location)
BASE_DIR = Path(__file__).resolve().parent

# Main directories
DATA_DIR = BASE_DIR / 'data'
IMAGES_DIR = BASE_DIR / 'images'
SCRIPTS_DIR = BASE_DIR / 'scripts'

# Data file paths
SALARIES_CSV = DATA_DIR / 'ds_salaries.csv'
ISO_CSV = DATA_DIR / 'iso_3166_data.csv'

# Generated chart image paths
EXPERIENCE_CHART = IMAGES_DIR / 'experience_salaries_chart.png'
OFFSHORE_CHART = IMAGES_DIR / 'offshore_salaries_chart.png'
COUNTRY_CHART = IMAGES_DIR / 'country_salaries_chart.png'
COMPANY_SIZE_CHART = IMAGES_DIR / 'company_size_chart.png'
REMOTE_CHART = IMAGES_DIR / 'remote_chart.png'

# Backward compatibility aliases
DIR_DADOS = DATA_DIR
DIR_IMAGENS = IMAGES_DIR
DIR_SCRIPTS = SCRIPTS_DIR
CSV_SALARIOS = SALARIES_CSV
CSV_ISO = ISO_CSV
GRAFICO_EXPERIENCIA = EXPERIENCE_CHART
GRAFICO_OFFSHORE = OFFSHORE_CHART
GRAFICO_PAISES = COUNTRY_CHART
GRAFICO_TAMANHO_EMPRESA = COMPANY_SIZE_CHART
GRAFICO_REMOTO = REMOTE_CHART
