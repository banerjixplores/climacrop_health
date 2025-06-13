# pages/01_Map.py

from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

# ───────── Page config & icon ─────────
ICON_PATH = Path(__file__).parent / "images" / "plant_health_logo.ico"
st.set_page_config(
    page_title="Geographic Analysis",
    page_icon="🌍",
    layout="wide",
)

# ───────── Reuse color-blind–safe CSS + story_box helper ─────────
st.markdown("""
<style>
/* reuse your existing box styles here… */
/* ───────── Story Intro Styling ───────── */
.story-intro {
  font-size: 1.4rem;            /* larger text */
  font-weight: 600;             /* semi-bold */
  text-align: center;
  margin: 24px 0;
  color: var(--text-color);
}
.story-intro span.highlight {
  color: var(--primary-color);
  font-style: italic;
}

.box-summary {
  background-color: #F7FCF5;
  border-left: 4px solid #C7E9C0;
  color: #0B3D0B;
  padding: 16px; margin: 16px 0;
}
.box-objectives {
  background-color: #E5F5E0;
  border-left: 4px solid #A1D99B;
  color: #0B3D0B;
  padding: 16px; margin: 16px 0;
}
</style>
""", unsafe_allow_html=True)

def story_box(items: list[str], style: str):
    cls = "box-summary" if style=="summary" else "box-objectives"
    html = f"<div class='{cls}'><ul>"
    for it in items:
        html += f"<li>{it}</li>"
    html += "</ul></div>"
    st.markdown(html, unsafe_allow_html=True)
    
# ───────── Title & Map Caption ─────────
st.markdown(
    "<h1 style='text-align:center; color:#2E7D32;'> Where Outbreaks Happen? </h1>",
    unsafe_allow_html=True
)

# ───────── Centered Map Embed ─────────
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    # replace with your actual map HTML or Streamlit chart call
    components.html(
        (Path(__file__).parent.parent / "images" / "global_map.html").read_text(encoding="utf-8"),
        height=600,
        width=800,
        scrolling=True
    )

with col2:
    st.markdown(
        """
        <p style='
            text-align: center;
            color: var(--text-color);
            font-size: 0.9rem;
            font-style: italic;
            margin-top: -8px;
        '>
            Color = mean monthly temperature; Shape = Agricultural vs. Wild
        </p>
        """,
        unsafe_allow_html=True
    )
# ───────── Caption for the Figure ─────────
st.markdown(
    """
    <div class='story-intro'>
      Map shows spatial distribution of disease observations; zoom and hover for details.
    </div>
    """,
    unsafe_allow_html=True
)

story_box([
    "Global database of plant‐disease records linked to weather & climate.",
    "Circles = agricultural surveys; diamonds = wild‐population surveys (4,339 total).",
    "Point color encodes mean temperature during each survey (°C)."
], style="summary")


# ───────── Insights for Technical Teams ─────────
st.markdown(
    """
    <div class='story-intro'>
      Insights for <strong>Technical Teams</strong>
    </div>
    """,
    unsafe_allow_html=True
)


story_box([
    "Strong clustering in mid-latitudes & Africa—check for spatial sampling bias.",
    "Color gradient spans 10–30 °C, indicating robust temperature coverage for modeling."
], style="objectives")

# ───────── Insights for Farmers ─────────
st.markdown(
    """
    <div class='story-intro'>
      Insights for <strong>Farmers</strong>
    </div>
    """,
    unsafe_allow_html=True
)
story_box([
    "Assess your region’s marker density to spot under- or over-sampling.",
    "Hover over points to compare local incidence rates and survey years."
], style="objectives")

# ───────── Insights for Environmental Agencies ─────────
st.markdown(
    """
    <div class='story-intro'>
      Insights for <strong>Environmental Agencies</strong>
    </div>
    """,
    unsafe_allow_html=True
)
story_box([
    "Identify ‘cold-spots’ (few surveys) to prioritize wild-plant disease monitoring.",
    "Use this map to guide resource allocation for new field surveys."
], style="objectives")


