# my_plant_disease_repo/notebook_style/00_notebook_style.py

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import HTML, display

# ====================================================
# 1) Seaborn + Matplotlib global style for all notebooks
# ====================================================
sns.set_theme(
    style="whitegrid",
    palette="colorblind",
    rc={
        "figure.dpi": 120,
        "axes.titlesize": 14,
        "axes.labelsize": 12,
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,
        "legend.frameon": False,
        "grid.linestyle": "--",
        "grid.alpha": 0.3,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.edgecolor": "#666",
        "axes.linewidth": 1.0,
    }
)

# ====================================================
# 2) Define color‐blind‐friendly colors for Wild vs. Ag (example)
# ====================================================
cb = sns.color_palette("colorblind")
WILD_COLOR = cb[2]   # greenish‐teal
AG_COLOR   = cb[0]   # navy‐blue

__all__ = ["np", "pd", "plt", "sns", "WILD_COLOR", "AG_COLOR"]

# ====================================================
# 3) Inject custom.css into the current notebook
# ====================================================
# We assume that `custom.css` lives in a folder named `notebook_style`
# which is a child of the current working directory (os.getcwd()).

css_path = os.path.join(os.getcwd(), "notebook_style", "custom.css")
if os.path.exists(css_path):
    with open(css_path, "r", encoding="utf-8") as f:
        css = f.read()
    # Wrap the CSS content in a <style> tag and display it so Jupyter will apply it
    display(HTML(f"<style>{css}</style>"))
else:
    print(f"⚠️  custom.css not found at: {css_path}; skipping CSS injection.")
