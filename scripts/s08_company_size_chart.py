# Imports
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import config
import matplotlib.pyplot as plt

# Import summary data calculated in s07_company_size_analysis
from scripts.s07_company_size_analysis import df_summary

# Prepare data for the chart
labels = df_summary.index
salaries = df_summary['Avg_Salary'].values
colors = ['#2b5c8f', '#3670a3', '#4682b4']

# Build the chart
fig, ax = plt.subplots(figsize=(8, 5.5))
bars = ax.bar(labels, salaries, color=colors, width=0.5)

for bar in bars:
    height = bar.get_height()
    ax.annotate(f'${height:,.2f}',
                xy=(bar.get_x() + bar.get_width() / 2.0, height),
                xytext=(0, 5),
                textcoords='offset points',
                ha='center', va='bottom',
                fontsize=10, fontweight='bold', color='#1d3557')

# Chart styling
ax.set_title('Average Salary by Company Size', fontsize=12, fontweight='bold', pad=15, color='#1d3557')
ax.set_xlabel('Company Size', fontsize=11, fontweight='bold', labelpad=10)
ax.set_ylabel('Average Salary (USD $)', fontsize=11, fontweight='bold', labelpad=10)

# Y-axis limit adjustment
max_val = float(salaries.max())
ax.set_ylim(0, max_val * 1.18)
ax.yaxis.set_major_formatter('${x:,.0f}')
ax.grid(axis='y', linestyle='--', alpha=0.5)
ax.set_axisbelow(True)

# Remove unnecessary spines
for spine in ['top', 'right', 'left']:
    ax.spines[spine].set_visible(False)

# Save the image
plt.tight_layout()
plt.savefig(config.GRAFICO_TAMANHO_EMPRESA, dpi=300, bbox_inches='tight')
plt.close()

print(f"\n✅ Chart saved successfully to: {config.GRAFICO_TAMANHO_EMPRESA}\n")
