# Imports
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import config
import pandas as pd

# Load dataset
df = pd.read_csv(config.CSV_SALARIOS, index_col=0)

# Map remote_ratio to descriptive names
remote_map = {
    0: 'In-person',
    50: 'Hybrid',
    100: 'Remote'
}
experience_map = {
    'EN': 'Entry-level (EN)',
    'MI': 'Mid-level (MI)',
    'SE': 'Senior (SE)',
    'EX': 'Executive (EX)'
}

df['work_model'] = df['remote_ratio'].map(remote_map)
df['exp_level_desc'] = df['experience_level'].map(experience_map)

exp_order = ['Entry-level (EN)', 'Mid-level (MI)', 'Senior (SE)', 'Executive (EX)']
model_columns = ['In-person', 'Hybrid', 'Remote']

# Select top 4 most frequent job titles
top_4_jobs = df['job_title'].value_counts().head(4).index.tolist()

# Dictionary to store the 4 pivot tables generated in loop
tables_by_job = {}

for job in top_4_jobs:
    df_job = df[df['job_title'] == job]

    table = df_job.pivot_table(
        index='exp_level_desc',
        columns='work_model',
        values='salary_in_usd',
        aggfunc='mean'
    ).reindex(exp_order)

    # Ensure all work model columns exist in the table
    for col in model_columns:
        if col not in table.columns:
            table[col] = float('nan')

    tables_by_job[job] = table[model_columns]

# Display the 4 tables in terminal
if __name__ == '__main__':
    print("\n" + "=" * 75)
    print("=== AVERAGE SALARY BY JOB TITLE, EXPERIENCE & WORK MODEL (USD $) ===")
    print("=" * 75 + "\n")

    for job, table in tables_by_job.items():
        print(f"📌 JOB TITLE: {job.upper()}")
        print("-" * 60)
        # Format display with $ without modifying the underlying numeric DataFrame
        formatted_table = table.map(lambda x: f'$ {x:,.2f}' if pd.notna(x) else '     -     ')
        print(formatted_table)
        print("\n" + "." * 75 + "\n")
