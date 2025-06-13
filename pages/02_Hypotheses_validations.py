from pathlib import Path
import streamlit as st
import pandas as pd

# ───────── Page config & icon ─────────
ICON_PATH = Path(__file__).parent / "images" / "plant_health_logo.ico"
st.set_page_config(
    page_title="Hypotheses & Validation",
    page_icon="🔬",
    layout="wide",
)

# ───────── Rationale & section CSS ─────────
st.markdown("""
<style>
/* Rationale section restyled for readability */
h2.rationale {
  color: var(--primary-color);
  margin-top: 1.5rem;
  margin-bottom: 0.5rem;
}
div.rationale-box {
  background: #E8F5E9;               /* very pale green */
  border-left: 6px solid var(--primary-color);  /* your primary green */
  color: var(--text-color);         /* dark text for max contrast */
  padding: 18px 22px 16px 22px;
  border-radius: 8px;
  margin-bottom: 1.5em;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
}
div.rationale-box ol li {
  margin-bottom: 0.7em;
}
div.rationale-box p, 
div.rationale-box ul {
  color: var(--text-color);
}
  /* ───────── Expander header styling ───────── */
div[data-testid="stExpander"] > div[role="button"],
div[data-testid="stExpander"] button[role="button"] {
  background-color: #C7E9C0 !important;    /* slightly darker pale-green */
  border-left:     4px solid #2E7D32 !important; /* dark-green accent */
  border-radius:   4px !important;
  padding:         8px 16px !important;
  margin-bottom:   8px !important;
}
/* Tint the arrow too */
div[data-testid="stExpander"] svg {
  stroke: #2E7D32 !important;
}
/* ───────── Custom green callout ───────── */
.callout-note {
  background-color: #E8F5E9;         /* pale green */
  border-left: 6px solid #2E7D32;    /* dark green accent */
  padding: 16px;
  margin: 16px 0;
  color: #1B5E20;                    /* dark-green text */
  border-radius: 4px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}
.callout-note strong {
  color: var(--primary-color);
}

</style>
""", unsafe_allow_html=True)

st.title("Hypotheses & Validation")
st.markdown(
    """
    <div class="callout-note">
      <strong>Note:</strong> Please expand each hypothesis to see:
      <ul>
        <li>What it means?</li>
        <li>How it was validated?</li>
        <li>Key results obtained</li>
        <li>Value-adds for researchers, farmers, and agencies</li>
      </ul>
    </div>
    """,
    unsafe_allow_html=True
)


# ───────── Hypothesis 1 ─────────
with st.expander("**Hypothesis 1: Weather, Anomaly & Historical Climate Effects**"):
    st.markdown(
        "**Each climate component (contemporaneous, anomaly, historical) independently influences disease incidence.**"
    )
    st.markdown("**Validation Approach:**")
    st.markdown("""
    - Computed temperature metrics `temp_anomaly_C`, `contemp_temp_C`, `annual_mean_temp_C`  
    - Computed precipitation metrics `rain_anomaly_daily`, `monthly_precip_mm_per_day`, `annual_precip_mm_per_day`  
    - Fitted linear & quadratic models for Wild vs. Agricultural; recorded R² and p-values
    """)
    df_temp = pd.DataFrame({
        "Metric": [
            "Temperature Anomaly",
            "Contemporary Temperature",
            "Historical Annual Temperature"
        ],
        "Wild R²": [0.0687, 0.0740, 0.1153],
        "Ag R²": [0.0071, 0.0698, 0.0359],
        "Wild p-linear": ["4.3e-10", "1.6e-09", "9.6e-14"],
        "Ag p-linear": ["1.3e-06", "4.5e-17", "7.2e-21"]
    })
    st.markdown("**Key Temperature Results**")
    st.table(df_temp)
    df_precip = pd.DataFrame({
        "Metric": [
            "Rainfall Anomaly",
            "Contemporary Precipitation",
            "Historical Monthly Precipitation",
            "Annual Precipitation"
        ],
        "Wild R²": [0.0134, 0.0365, 0.0134, 0.0089],
        "Ag R²": [0.0590, 0.0242, 0.0590, 0.0313],
        "Wild p": ["6.6e-03", "2.0e-05", "6.7e-03", "2.8e-02"],
        "Ag p": ["3.8e-06", "7.5e-07", "3.7e-06", "3.9e-08"]
    })
    st.markdown("**Key Precipitation Results**")
    st.table(df_precip)
    st.markdown("**Conclusion:** Hypothesis 1 is validated—each climate factor significantly influences disease, with wild systems generally more sensitive.")
    st.markdown("#### Stakeholder Insights")
    st.markdown("""
    - **Researchers:** Use CV-validated metrics to refine predictive models across systems.  
    - **Farmers:** Monitor both anomalies and contemporary weather to anticipate outbreaks.  
    - **Agencies:** Prioritize monitoring in regions where wild systems show highest climate sensitivity.
    """)

# ───────── Hypothesis 2 ─────────
with st.expander("**Hypothesis 2: System-Type Sensitivity**"):
    st.markdown(
        "**Wild plant–pathogen systems exhibit stronger climate–disease responses than agricultural systems.**"
    )
    st.markdown("**Validation Approach:** Compared R² for each metric between Wild vs. Ag.")
    df_h2 = pd.DataFrame({
        "Metric": [
            "Annual Historical Temp",
            "Temp Anomaly",
            "Contemporary Temp",
            "Annual Precipitation",
            "Precipitation Anomaly",
            "Contemporary Precipitation",
            "Monthly Historical Precipitation"
        ],
        "Wild R²": [0.1153, 0.0687, 0.0740, 0.0089, 0.0134, 0.0365, 0.0134],
        "Ag R²": [0.0359, 0.0071, 0.0698, 0.0313, 0.0590, 0.0242, 0.0590],
        "Wild > Ag?": ["yes", "yes", "slightly", "no", "no", "yes", "no"]
    })
    st.markdown("**Wild vs. Ag R² Comparison**")
    st.table(df_h2)
    st.markdown("**Conclusion:** Wild > Ag for all temperature metrics; precipitation shows mixed sensitivity.")
    st.markdown("#### Stakeholder Insights")
    st.markdown("""
    - **Researchers:** Focus on wild-system data for understanding extreme-weather impacts.  
    - **Farmers:** Recognize that crops have buffered responses—management matters.  
    - **Agencies:** Allocate resources to wild-system studies where the climate signal is strongest.
    """)

# ───────── Hypothesis 3 ─────────
with st.expander("**Hypothesis 3: Thermal & Precipitation Mismatch**"):
    st.markdown(
        "**In wild systems, disease spikes at moderate deviations from historical norms; agriculture shows little mismatch.**"
    )
    st.markdown("**Validation Approach:** OLS with interaction `anomaly × historical` for each system.")
    df_h3 = pd.DataFrame({
        "Effect": ["Temp × Historical", "Rain × Historical"],
        "Wild Coef.": [-0.0142, -0.0312],
        "Ag Coef.": [-0.0031, -0.0069],
        "p-value": ["< 0.001", "< 0.01"]
    })
    st.markdown("**Interaction Coefficients**")
    st.table(df_h3)
    st.markdown("**Conclusion:** Wild systems confirm a strong mismatch effect; agriculture is largely buffered.")
    st.markdown("#### Stakeholder Insights")
    st.markdown("""
    - **Researchers:** Incorporate mismatch interactions in risk models for wild ecosystems.  
    - **Farmers:** Expect milder mismatch effects—focus on overall warming trends.  
    - **Agencies:** Use mismatch patterns to trigger early-warning for wild-plant monitoring.
    """)

# ───────── Hypothesis 4 ─────────
with st.expander("**Hypothesis 4: Geographic & Pathogen-Type Modulation**"):
    st.markdown(
        "**Pathogen identity and tolerance breadth shape climate–disease relationships.**"
    )
    st.markdown("**Validation Approach:** OLS with `anomaly × pathogen_group` and `anomaly × tolerance_class`.")
    df_pgroup = pd.DataFrame({
        "Pathogen Group": ["Eukaryotic parasite", "Pest", "Virus"],
        "Interaction Coef.": [-0.0124, -0.0076, -0.0335],
        "p-value": ["0.545", "0.812", "0.099"]
    })
    st.markdown("**Temp × Pathogen Group**")
    st.table(df_pgroup)
    df_tolerance = pd.DataFrame({
        "Tolerance Class": ["Intermediate", "Narrow"],
        "Interaction Coef.": [-0.0196, 0.0048],
        "p-value": ["0.003", "0.848"]
    })
    st.markdown("**Tolerance Class Effect**")
    st.table(df_tolerance)
    st.markdown("**Conclusion:** Pathogen identity alone isn’t significant; tolerance breadth shows a weak effect.")
    st.markdown("#### Stakeholder Insights")
    st.markdown("""
    - **Researchers:** Explore regional pathogen profiles for tailored models.  
    - **Farmers:** Understand which pathogen groups may respond sharply to anomalies.  
    - **Agencies:** Target surveillance by pathogen type and tolerance class in critical zones.
    """)

# ───────── Hypothesis 5 ─────────
with st.expander("**Hypothesis 5: Transmission-Mode Sensitivity**"):
    st.markdown(
        "**Directly transmitted pathogens respond more strongly to precipitation anomalies than vector-borne ones.**"
    )
    st.markdown("**Validation Approach:** OLS with `abs_precip_anom × C(transmission_mode)`.")
    df_h5 = pd.DataFrame({
        "Term": [
            "Intercept (Direct slope)",
            "Vector-borne main effect",
            "Direct slope",
            "Slope difference (Vector vs Direct)"
        ],
        "Coefficient": [0.1171, -0.0414, 0.0505, -0.0150],
        "p-value": ["< 0.001", "0.040", "< 0.001", "0.062"]
    })
    st.markdown("**Precipitation × Transmission Mode**")
    st.table(df_h5)
    st.markdown("**Conclusion:** Direct pathogens have steeper precipitation-response; vector-borne are somewhat buffered.")
    st.markdown("#### Stakeholder Insights")
    st.markdown("""
    - **Researchers:** Factor in transmission mode when modeling moisture-driven disease.  
    - **Farmers:** Watch for direct-pathogen outbreaks after heavy rain or drought.  
    - **Agencies:** Allocate monitoring efforts by transmission mode to anticipate outbreak pathways.
    """)

# ───────── Rationale Behind the Five Hypotheses ─────────
st.markdown('<h2 class="rationale">Rationale Behind the Five Hypotheses</h2>', unsafe_allow_html=True)
st.markdown("""
<div class="rationale-box">
<ol>
  <li><strong>Hypotheses 1–3</strong> adapt core findings from Kirk et al. (2025), grounding our EDA in peer-reviewed results.</li>
  <li><strong>Hypothesis 4</strong> extends the work by testing geographic and pathogen identity effects not fully explored in the original paper.</li>
  <li><strong>Hypothesis 5</strong> adds transmission mode, reflecting ecological mechanisms of vector versus direct spread.</li>
</ol>
<p style="margin-top:1em;">
  <strong>Together, these five hypotheses:</strong>
  <ul style="margin-left:1.2em;">
    <li>Anchor our analysis in established science</li>
    <li>Expand to pathogen ecology and geography</li>
    <li>Deliver actionable insights for researchers, farmers, and agencies</li>
  </ul>
</p>
</div>
""", unsafe_allow_html=True)
