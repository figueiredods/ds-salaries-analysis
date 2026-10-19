# Imports
import sys
from pathlib import Path

# Adjust path to locate config.py in the project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

import config
import matplotlib.pyplot as plt

# Import processed data from s04_geographic_analysis
from scripts.s04_geographic_analysis import df_us_grouped

# Define labels, values, and colors
labels = ['USA (Local)', 'Offshore (Remote)']
salaries = df_us_grouped.values
colors = ['#2b5c8f', '#3670a3']

# Create figure
fig, ax = plt.subplots(figsize=(8, 5.5))

# Configure bars
bars = ax.bar(labels, salaries, color=colors, width=0.45)

# Add value annotations above bars
for bar in bars:
    height = bar.get_height()
    ax.annotate(
        f'${height:,.2f}',
        xy=(bar.get_x() + bar.get_width() / 2.0, height),
        xytext=(0, 5),
        textcoords='offset points',
        ha='center',
        va='bottom',
        fontsize=10,
        fontweight='bold',
        color='#1d3557'
    )

# Chart styling
ax.set_title('Average Salary in US Companies: Local vs. Offshore', fontsize=12, fontweight='bold', pad=15, color='#1d3557')
ax.set_xlabel('Employee Location', fontsize=11, fontweight='bold', labelpad=10)
ax.set_ylabel('Average Salary (USD $)', fontsize=11, fontweight='bold', labelpad=10)

ax.set_ylim(0, max(salaries) * 1.18)
ax.yaxis.set_major_formatter('${x:,.0f}')
ax.grid(axis='y', linestyle='--', alpha=0.5)
ax.set_axisbelow(True)

# Remove unnecessary spines
for spine in ['top', 'right', 'left']:
    ax.spines[spine].set_visible(False)

# Save chart image and close plot
plt.tight_layout()
plt.savefig(config.GRAFICO_OFFSHORE, dpi=300, bbox_inches='tight')
plt.close()

print(f"\n✅ Chart saved successfully to: {config.GRAFICO_OFFSHORE}\n")
