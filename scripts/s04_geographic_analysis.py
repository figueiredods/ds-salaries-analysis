# Imports
import sys
from pathlib import Path

# Adjust path to locate config.py in the project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

import pandas as pd
import config

# Load dataset
df = pd.read_csv(config.CSV_SALARIOS, index_col=0)

# MAINTENANCE NOTE: We use 'keep_default_na=False' to prevent Pandas from interpreting 'NA' (Namibia) as a null value (NaN).
df_iso = pd.read_csv(config.CSV_ISO, keep_default_na=False)

# INTEGRITY VALIDATION - Ensure no country code is empty before proceeding
assert df_iso['Code'].isna().sum() == 0, "Error: There are null ISO codes in the country table!"

# Map country names
df_iso = df_iso.set_index('Code')
df['residence_country'] = df['employee_residence'].map(df_iso['Name'])
df['company_country'] = df['company_location'].map(df_iso['Name'])

# Create Offshore column (residence country != company country)
df["offshore"] = df['employee_residence'] != df['company_location']

# -- PROCESSING 1: US COMPANIES (LOCAL VS OFFSHORE)
df_us = df[df['company_location'] == 'US']
df_us_grouped = df_us.groupby('offshore')['salary_in_usd'].mean()

boolean_names = {
    False: 'USA',
    True: 'Offshore'
}

df_summary = pd.DataFrame({
    'Avg_Salary': df_us_grouped,
    'Absolute_Difference': df_us_grouped.diff(periods=-1),
    'Percentage_Variation': df_us_grouped.pct_change(periods=-1) * 100
})

# -- PROCESSING 2: SALARY BY RESIDENCE COUNTRY
df_filtered_countries = df.groupby('residence_country')['salary_in_usd'].agg(['count', 'mean', 'median']).query('count >= 5').sort_values(by='mean', ascending=False)

# --- TERMINAL DISPLAY (Runs only when executed directly) ---
if __name__ == '__main__':
    print("\n" + "~" * 65)
    print("=== OFFSHORE WORK ANALYSIS IN US COMPANIES ===")
    print("~" * 65)
    print(f"{'Location':<20} | {'Avg Salary':<15} | {'Difference':<25}")
    print("~" * 65)

    # Iterate and format display
    for local, row in df_summary.iterrows():
        display_name = boolean_names[local]
        formatted_salary = f"${row['Avg_Salary']:>11,.2f}"

        if pd.isna(row['Absolute_Difference']):
            diff_str = "-"
        else:
            abs_val = f"+$ {row['Absolute_Difference']:,.2f}"
            pct_val = f"(+ {row['Percentage_Variation']:.1f}%)"
            diff_str = f"{abs_val} {pct_val}"
        print(f"{display_name:<20} | {formatted_salary:<15} | {diff_str:<25}")

    print("~" * 65 + "\n")

    print("=== AVERAGE/MEDIAN SALARY BY RESIDENCE COUNTRY (COUNT >= 5) ===")
    print(df_filtered_countries.map(lambda x: f'$ {x:,.2f}'))
