from pathlib import Path
from IPython.display import HTML, display
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def load_style():
    # Set visual style
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

    # Colors
    cb = sns.color_palette("colorblind")
    globals()["WILD_COLOR"] = cb[2]
    globals()["AG_COLOR"] = cb[0]

    # Inject CSS relative to this script
    style_dir = Path(__file__).parent
    css_path = style_dir / "custom.css"
    if css_path.exists():
        try:
            css = css_path.read_text(encoding='utf-8')
            display(HTML(f"<style>{css}</style>"))
            print(f"Injected custom CSS from: {css_path}")
        except Exception as e:
            print(f"Failed to load custom.css: {e}")
    else:
        print(f"custom.css not found at: {css_path}")
