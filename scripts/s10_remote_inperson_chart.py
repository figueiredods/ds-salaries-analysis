# Imports
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import config
import matplotlib.pyplot as plt
import numpy as np

# Import the 4 tables generated in script 09
from scripts.s09_remote_inperson_analysis import tables_by_job

# 2x2 Grid figure configuration
fig, axes = plt.subplots(2, 2, figsize=(14, 10), sharey=True)
flat_axes = axes.flatten()

# Simplified labels for the X-axis
x_labels = ['Junior', 'Mid-level', 'Senior', 'Executive']
x = np.arange(len(x_labels))
width = 0.25

colors = {'In-person': '#2b5c8f', 'Hybrid': '#e67e22', 'Remote': '#2ca02c'}

# Loop to draw each of the 4 jobs in a quadrant
for i, (job, table) in enumerate(tables_by_job.items()):
    ax = flat_axes[i]

    # Bar offsets for In-person, Hybrid, and Remote
    ax.bar(x - width, table['In-person'], width, label='In-person', color=colors['In-person'])
    ax.bar(x, table['Hybrid'], width, label='Hybrid', color=colors['Hybrid'])
    ax.bar(x + width, table['Remote'], width, label='Remote', color=colors['Remote'])

    # Individual quadrant styling
    ax.set_title(job, fontsize=12, fontweight='bold', color='#1d3557', pad=10)
    ax.set_xticks(x)
    ax.set_xticklabels(x_labels, fontsize=9, fontweight='bold')
    ax.yaxis.set_major_formatter('${x:,.0f}')
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    ax.set_axisbelow(True)

    for spine in ['top', 'right', 'left']:
        ax.spines[spine].set_visible(False)

# Single legend at the top of the figure
handles, labels = flat_axes[0].get_legend_handles_labels()
fig.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5, 0.98), ncol=3, fontsize=11, frameon=False)

# Main Title
fig.suptitle('Average Salary by Job Title, Experience Level & Work Model', fontsize=15, fontweight='bold', color='#1d3557', y=1.02)

# Save image
plt.tight_layout()
plt.savefig(config.GRAFICO_REMOTO, dpi=300, bbox_inches='tight')
plt.close()

print(f"\n✅ 2x2 Panel chart saved successfully to: {config.GRAFICO_REMOTO}\n")
