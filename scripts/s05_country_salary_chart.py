# Imports
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import config
import matplotlib.pyplot as plt

# Import filtered and processed data from script 04
from s04_geographic_analysis import df_filtered_countries

# Sort from lowest to highest for horizontal bar chart display
df_means = df_filtered_countries.sort_values(by='mean', ascending=True)

# Create figure
fig, ax = plt.subplots(figsize=(10, 6))

# Configure horizontal bars
bars = ax.barh(df_means.index, df_means['mean'], color='#2b5c8f', height=0.6)

# Value labels at the end of each bar
for bar in bars:
    width = bar.get_width()
    ax.annotate(f'${width:,.0f}',
        xy=(width, bar.get_y() + bar.get_height() / 2),
        xytext=(6, 0),
        textcoords='offset points',
        ha='left', va='center', fontsize=9, fontweight='bold', color='#1d3557')

# Styling
ax.set_title('Average Salary by Country of Residence (Sample ≥ 5)', fontsize=13, fontweight='bold', pad=15, color='#1d3557')
ax.set_xlabel('Average Annual Salary (USD $)', fontsize=11, fontweight='bold', labelpad=10)
ax.set_ylabel('Country of Residence', fontsize=11, fontweight='bold', labelpad=10)

ax.set_xlim(0, df_means['mean'].max() * 1.15)
ax.xaxis.set_major_formatter('${x:,.0f}')
ax.grid(axis='x', linestyle='--', alpha=0.5)
ax.set_axisbelow(True)

# Remove unnecessary spines
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)

# Save image to project folder
plt.tight_layout()
plt.savefig(config.GRAFICO_PAISES, dpi=300, bbox_inches='tight')
plt.close()

print(f"\n✅ Chart successfully saved to: {config.GRAFICO_PAISES}\n")
