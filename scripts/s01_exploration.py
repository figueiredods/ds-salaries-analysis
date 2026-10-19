# Imports
import sys
from pathlib import Path

# Adjust path to locate config.py in the project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

import pandas as pd
import config

# 1. Load dataset
df = pd.read_csv(config.CSV_SALARIOS, index_col=0)

# 2. Display the first 5 rows
print(" --- FIRST ROWS --- ")
print(df.head())

# 3. DataFrame Information and Statistics
print("\n --- DATAFRAME INFO --- ")
print(df.info())

print("\n --- DATAFRAME STATISTICS --- ")
print(df['salary_in_usd'].describe().map(lambda x: f'$ {x:,.2f}'))

# 4. Number of distinct job titles in the DataFrame
n_job_titles = df["job_title"].nunique()

# 5. List of distinct job titles and their counts
job_title_counts = df["job_title"].value_counts()

print(f"\n --- TOTAL DISTINCT JOB TITLES: {n_job_titles} --- ")

print(f"\n --- TOP 5 JOB TITLES (COUNT PER JOB) ---")
print(job_title_counts.head())

# 6. Global average salary in USD
global_avg_salary = df["salary_in_usd"].mean()

print(f"\n --- GLOBAL AVERAGE SALARY (USD $): {global_avg_salary:,.2f} ---\n")

# 7. Highest and Lowest salary with their respective job titles
idx_max = df['salary_in_usd'].idxmax()  # Returns the index of the maximum value in 'salary_in_usd'
idx_min = df['salary_in_usd'].idxmin()

highest_salary = df.loc[idx_max, 'salary_in_usd']
highest_salary_job = df.loc[idx_max, 'job_title']

lowest_salary = df.loc[idx_min, 'salary_in_usd']
lowest_salary_job = df.loc[idx_min, 'job_title']

print(f"\n --- HIGHEST SALARY (USD $): ${highest_salary:,.2f} ---")
print(f" --- JOB TITLE: {highest_salary_job} ---\n")

print(f"\n --- LOWEST SALARY (USD $): ${lowest_salary:,.2f} ---")
print(f" --- JOB TITLE: {lowest_salary_job} ---\n")
