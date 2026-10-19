# Imports
import sys
from pathlib import Path

# Adjust path to locate config.py in the project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

import pandas as pd
import config

# Load data
df = pd.read_csv(config.CSV_SALARIOS, index_col=0)

# Map size codes to descriptive labels
size_map = {
    'S': 'Small (<50)',
    'M': 'Medium (50 - 250)',
    'L': 'Large (>250)'
}

# Organize by size order
size_order = ['Small (<50)', 'Medium (50 - 250)', 'Large (>250)']

df['company_size_desc'] = df['company_size'].map(size_map)

# Group by size and calculate metrics
df_grouped_company_size = df.groupby('company_size_desc')['salary_in_usd'].mean().reindex(size_order)

df_summary = pd.DataFrame({
    'Avg_Salary': df_grouped_company_size,
    'Absolute_Difference': df_grouped_company_size.diff(periods=1),
    'Percentage_Variation': df_grouped_company_size.pct_change(periods=1) * 100
})

if __name__ == '__main__':
    print("\n" + "~" * 65)
    print("=== AVERAGE SALARY ANALYSIS BY COMPANY SIZE ===")
    print("~" * 65)
    print(f"{'Company Size':<20} | {'Average Salary':<15} | {'Difference':<25}")
    print("~" * 65)

    # Iterate and format output display
    for size, row in df_summary.iterrows():
        display_name = size
        formatted_salary = f"${row['Avg_Salary']:>11,.2f}"

        if pd.isna(row['Absolute_Difference']):
            increase_str = "-"
        else:
            abs_val = f"+$ {row['Absolute_Difference']:,.2f}"
            pct_val = f"(+ {row['Percentage_Variation']:.1f}%)"
            increase_str = f"{abs_val} {pct_val}"
        print(f"{display_name:<20} | {formatted_salary:<15} | {increase_str:<25}")

    print("~" * 65 + "\n")
