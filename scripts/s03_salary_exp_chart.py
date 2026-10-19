# Imports
import sys
from pathlib import Path

# Adjust path to locate config.py in the project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

import config
import matplotlib.pyplot as plt

# Import data calculated in s02_salary_exp_analysis
from s02_salary_exp_analysis import df_summary, level_names

# Define descriptive labels and values
labels = [level_names[level] for level in df_summary.index]
values = df_summary['Avg_Salary']

# Create figure
fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(labels, values, color='#2b5c8f')

ax.set_title('Average Salary by Experience Level', fontsize=12, fontweight='bold')  # Title
ax.set_ylabel('Annual Salary (USD $)', fontsize=10)  # Y-axis
ax.yaxis.set_major_formatter('$ {x:,.0f}')
ax.grid(axis='y', linestyle='--', alpha=0.5)

# Save image in the project folder and close
plt.tight_layout()
plt.savefig(config.GRAFICO_EXPERIENCIA, dpi=300, bbox_inches='tight')
plt.close()

print(f"\n✅ Experience Chart saved to: {config.GRAFICO_EXPERIENCIA}\n")
