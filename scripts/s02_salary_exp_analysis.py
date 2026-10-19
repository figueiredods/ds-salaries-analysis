# Imports
import sys
from pathlib import Path

# Adjust path to locate config.py in the project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

import pandas as pd
import config

# 1. Load dataset
df = pd.read_csv(config.CSV_SALARIOS, index_col=0)

# 2. Group by experience level
career_order = ["EN", "MI", "SE", "EX"]
avg_salary_exp = (
    df.groupby("experience_level")["salary_in_usd"]
    .mean()
    .reindex(career_order)
)

# 3. Create a summary DataFrame with absolute difference and percentage change
df_summary = pd.DataFrame({
    "Avg_Salary": avg_salary_exp,
    "Absolute_Increase": avg_salary_exp.diff(),  # Subtracts current value from previous row's value
    "Percentage_Increase": avg_salary_exp.pct_change() * 100,  # Calculates percentage change between current and previous row
})

# 4. Map descriptive names for display
level_names = {
    "EN": "EN (Entry-level)",
    "MI": "MI (Mid-level)",
    "SE": "SE (Senior)",
    "EX": "EX (Executive)",
}

# 5. Print formatted table
if __name__ == "__main__":
    print("\n" + "=" * 70)
    print(
        f"{'Experience Level':<20} | {'Average Salary':<15} | {'Increase vs Previous Level':<25}"
    )  # <20 is left alignment formatting
    print("=" * 70)

    # Iterate over each row and format display
    for level, row in df_summary.iterrows():
        display_name = level_names[level]
        formatted_salary = f"${row['Avg_Salary']:>11,.2f}"  # >11 is right alignment formatting

        # If Entry-level (first row), there is no previous level
        if pd.isna(row["Absolute_Increase"]):  # Checks if row value in column is NaN
            increase_str = "-" * 10
        else:
            abs_val = f"+ ${row['Absolute_Increase']:>10,.2f}"
            pct_val = f"(+ {row['Percentage_Increase']:.1f}%)"
            increase_str = f"{abs_val}  {pct_val}"

        # Print formatted row with fixed column widths
        print(f"{display_name:<20} | {formatted_salary:<15} | {increase_str:<25}")

    print("-" * 70 + "\n")
