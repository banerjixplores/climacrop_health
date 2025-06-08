# my_plant_disease_repo/notebook_style/00_notebook_style.py

from pathlib import Path
from IPython.display import HTML, display
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


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

# CSS injection using STYLE_PATH
try:
    style_dir = Path(STYLE_PATH).parent
except NameError:
    raise RuntimeError("STYLE_PATH not defined. Run via load_style() from style_loader.")
css_path = style_dir / "custom.css"

if css_path.exists():
    try:
        css = css_path.read_text(encoding='utf-8')
        display(HTML(f"<style>{css}</style>"))
        print(f"Injected custom CSS from: {css_path}")
    except UnicodeDecodeError as e:
        print(f"Failed to read CSS due to encoding error: {e}")
else:
    print(f"custom.css not found at: {css_path}; skipping CSS injection.")
