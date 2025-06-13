import streamlit as st
from pathlib import Path

# Build the correct path to your icon folder
ICON_PATH = Path(__file__).parent / "images" / "plant_health_logo.ico"

st.set_page_config(
    page_title="Plant Health Dashboard",
    page_icon=str(ICON_PATH),    # Streamlit will load the .ico for you
    layout="wide",
)

# ───────── Colorblind-safe CSS for story boxes ─────────
st.markdown("""
<style>
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
  background-color: #F7FCF5;    /* very pale green */
  border-left: 4px solid #C7E9C0; /* light medium green */
  color: #0B3D0B;               /* dark green text */
}
.box-objectives {
  background-color: #E5F5E0;    /* pale green */
  border-left: 4px solid #A1D99B; /* medium green */
  color: #0B3D0B;
}
.box-requirements {
  background-color: #C7E9C0;    /* light medium green */
  border-left: 4px solid #74C476; /* brighter green */
  color: #0B3D0B;
}
.box-dataset {
  background-color: #A1D99B;    /* medium green */
  border-left: 4px solid #41AB5D; /* strong green */
  color: #0B3D0B;
}
.box-details {
  background-color: #74C476;     /* bright green */
  border-left: 4px solid #00441B;/* very dark green */
  padding: 16px;
  margin: 16px 0;
  color: white;
  font-size: 0.95rem;
  line-height: 1.4;
}
.box-summary ul,
.box-objectives ul,
.box-requirements ul,
.box-dataset ul,
.box-details ul {
  margin: 0;
  padding-left: 1.2em;
}
.box-summary li,
.box-objectives li,
.box-requirements li,
.box-dataset li,
.box-details li {
  margin-bottom: 8px;
}
</style>
""", unsafe_allow_html=True)

def story_box(items: list[str], style: str):
    cls = {
        "summary":      "box-summary",
        "objectives":   "box-objectives",
        "requirements": "box-requirements",
        "dataset":      "box-dataset",
        "details":      "box-details"
    }[style]
    html = f"<div class='{cls}'><ul>\n"
    for it in items:
        html += f"  <li>{it}</li>\n"
    html += "</ul></div>"
    st.markdown(html, unsafe_allow_html=True)

# ───────── Title & Intro ─────────
st.markdown(
    "<h1 style='text-align:center; color:#2E7D32;'>🍃 ClimaCrop Health: Plant Disease & Climate Impact Analysis</h1>",
    unsafe_allow_html=True
)

# Center the hero image by placing it in the middle of three columns
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.image(
        "images/header_disease_leaf.jpg",
        use_container_width=True,
        caption=(
            "Rose Black Spot (*Diplocarpon rosae*) – characteristic black lesions "
            "and yellowing. Image courtesy of Efekto blog "
            "(https://efekto.co.za/blog/blog/how-to-spot-and-treat-plant-diseases-for-a-thriving-garden/)"
        )
    )

st.markdown(
    """
    <div class='story-intro'>
      Welcome to <strong>ClimaCrop Health</strong>—an interactive dashboard weaving together  
      plant-disease surveys and climate records to tell a <span class="highlight">data-driven story</span>  
      of how weather shapes outbreaks in both natural ecosystems and our farms.
    </div>
    """,
    unsafe_allow_html=True
)


# ───────── Project Summary ─────────
story_box([
    "Brings together <strong>4,339</strong> plant-disease surveys linked to climate data from 1984–2019.",
    (
        "Answers <strong>Where</strong> outbreaks occur, "
        "<strong>How</strong> anomalies drive disease, "
        "<strong>Which</strong> climate metrics matter most, "
        "<strong>Who</strong> (pathogen groups) are high-risk, and "
        "<strong>What</strong> our models reveal."
    )
], style="summary")

st.markdown(
    """
    <div class='story-intro'>
      With this foundation, we set out to <span class="highlight">quantify the climate drivers</span> of disease  
      and build tools that stakeholders can trust.
    </div>
    """,
    unsafe_allow_html=True
)
# ───────── Project Objectives ─────────
story_box([
    "<strong>Quantify Climate Drivers:</strong> Measure contemporaneous weather, anomalies, and long-term climate effects.",
    "<strong>Compare Sensitivity:</strong> Show wild communities react more sharply to swings than irrigated crops.",
    "<strong>Detect Mismatch Effects:</strong> Find anomaly 'sweet spots' where disease risk peaks then declines.",
    "<strong>Predict & Visualize:</strong> Provide a concise model and interactive dashboard for scenario testing.",
    "<strong>Ensure Transparency:</strong> Fully document all cleaning, feature-engineering, and modeling steps."
], style="objectives")

st.markdown(
    """
    <div class='story-intro'>
      To turn these objectives into actionable insights, the dashboard supports the following requirements:
    </div>
    """,
    unsafe_allow_html=True
)

# ───────── Business Requirements ─────────
story_box([
    "<strong>Risk Forecasting:</strong> Input custom temperature & rainfall scenarios to output disease-risk scores.",
    "<strong>Risk Zoning:</strong> Classify locations into Low/Medium/High risk for rapid decision-making.",
    "<strong>Global Hotspot Mapping:</strong> Interactive world map of current or hypothetical risk zones.",
    "<strong>Interactive Scenario Testing:</strong> Sliders for non-technical users to ask 'What if June is +3 °C?'.",
    "<strong>Driver Explanation:</strong> Bullet out the top two climate drivers so stakeholders know **why** risk changes."
], style="requirements")

st.markdown(
    """
    <div class='story-intro'>
      All insights rest on a robust, reproducible dataset:
    </div>
    """,
    unsafe_allow_html=True
)

# ───────── Dataset Sources and Content ─────────
story_box([
    "Contains <strong>5,906</strong> plant–disease observations (1984–2019) from over 4,300 global studies.",
    "Paired with ERA5-land monthly data and 30-year WorldClim normals for anomaly calculation.",
    "Each record includes host, parasite, location, infected count, plus climate metrics "
    "(e.g., historical `bio01`, precipitation `bio12`, and recent anomalies).",
    'Source: <a href="https://doi.org/10.5061/dryad.p8cz8wb0h" target="_blank">'
    'Dryad Repository – DOI 10.5061/dryad.p8cz8wb0h</a>'
], style="dataset")
st.markdown("""
<div class="callout-note">
  <strong>Data Sources</strong><br>
  <ul>
    <li><b>Disease Surveys (1984–2019):</b>
      <ul>
        <li>Collated from peer‐reviewed publications via a systematic literature search.</li>
        <li>Each record includes:
          <ul>
            <li><b>Host species</b> (scientific name, order)</li>
            <li><b>Pathogen category</b> (virus, bacteria, eukaryotic parasite, pest)</li>
            <li><b>System type</b> (natural vs. agricultural)</li>
            <li><b>Sampling window</b> (start/end month) and <b>sample size</b> (n_total, n_infected)</li>
            <li><b>Location</b> (latitude, longitude; geocoded if needed)</li>
          </ul>
        </li>
      </ul>
    </li>
    <li><b>Climate & Weather Data:</b>
      <ul>
        <li><b>Historical Monthly Normals (Hₘ):</b> 30-year monthly averages (1960–1990) for temperature and precipitation from WorldClim V1.</li>
        <li><b>Historical Annual Climate (Hₐ):</b> 30-year annual means (WorldClim BIO1 and BIO12).</li>
        <li><b>Contemporaneous Weather (W):</b> Monthly mean temperature and total precipitation during each survey window, pulled via Google Earth Engine from ERA5-Land (aggregated to site coordinates).</li>
      </ul>
    </li>
    <li><b>Pathogen Metadata:</b>
      <ul>
        <li>Additional lookup tables for pathogen thermal/moisture niche breadth (if available).</li>
        <li>Transmission mode labels (vector‐borne vs. direct).</li>
      </ul>
    </li>
  </ul>
</div>
""", unsafe_allow_html=True)

st.markdown(
    """
    <div class='story-intro'>
      Use the sidebar navigation to explore model performance, rankings, and feature importances—
      all designed to guide farmers, agronomists, and conservationists in making climate-smart decisions.
    </div>
    """,
    unsafe_allow_html=True
)


st.markdown(
    """
    <div class='box-details'>
      For full details, see the 
      <a href="https://github.com/banerjixplores/climacrop_health#readme" target="_blank">
        GitHub README
      </a>.
    </div>
    """,
    unsafe_allow_html=True
)
