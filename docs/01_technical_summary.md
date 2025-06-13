## Technical Summary

### Project Overview
This repository implements a capstone project analyzing how short‐term weather anomalies and long‐term climate influence plant disease prevalence in both wild and agricultural systems. The analysis reproduces and extends methods from Kirk et al. (2025) and integrates them into a reproducible pipeline:

1. **Data Ingestion & Cleaning** – Acquire raw surveys of plant disease prevalence, geolocate each record, and merge with meteorological data.
2. **Feature Engineering** – Compute monthly anomalies (actual minus 30-year normals) for temperature and precipitation, plus extract historical annual climate.
3. **Modeling** – Fit binomial GLMMs to quantify the independent effects of contemporaneous weather (W), anomalies (A), and historical climate (Hₐ) on disease prevalence (P), separately for wild vs. agricultural systems.
4. **Visualization** – Generate diagnostic plots (e.g., prevalence vs. anomaly curves, marginal effects) and interactive dashboards (Streamlit) to explore geographic and pathogen‐type patterns.
5. **Extensions** – Implement additional hypotheses (e.g., pathogen niche breadth, transmission‐mode effects) using randomized slopes or interaction terms.

All code is organized into Jupyter notebooks for step‐by‐step reproducibility, plus a Streamlit app for stakeholder‐friendly visualization.

---

### Data Sources
- **Disease Surveys (1984–2019):**  
  - Collated from peer‐reviewed publications via a systematic literature search.  
  - Each record includes:  
    - **Host species** (scientific name, order)  
    - **Pathogen category** (virus, bacteria, eukaryotic parasite, pest)  
    - **System type** (wild vs. agricultural)  
    - **Sampling window** (start/end month) and **sample size** (n_total, n_infected)  
    - **Location** (latitude, longitude; geocoded if needed)
- **Climate & Weather Data:**  
  - **Historical Monthly Normals (Hₘ):** 30-year monthly averages (1960–1990) for temperature and precipitation from WorldClim V1.  
  - **Historical Annual Climate (Hₐ):** 30-year annual means (WorldClim BIO1 and BIO12).  
  - **Contemporaneous Weather (W):**  
    - Monthly mean temperature and total precipitation during each survey window, pulled via Google Earth Engine from ERA5-Land (aggregated to site coordinates).  
- **Pathogen Metadata:**  
  - Additional lookup tables for pathogen thermal/moisture niche breadth (if available).  
  - Transmission mode labels (vector‐borne vs. direct).

---

### Feature Engineering & Preprocessing
1. **Geolocation & Time‐Window Matching:**  
   - For records missing exact coordinates, approximate using Google Maps API based on site description.  
   - Ensure each survey’s “month(s)” align with corresponding ERA5 aggregation (e.g., if survey spanned March–April 2012, compute W for those two months).  
2. **Anomaly Calculations:**  
   - **Temperature Anomaly (Aᵀ):** Aᵀ = Wᵀ_{survey} – Hₘᵀ_{same month}  
   - **Precipitation Anomaly (Aᵖ):** Aᵖ = Wᵖ_{survey} – Hₘᵖ_{same month}  
3. **Data Filtering:**  
   - Exclude observations lacking any of W, Hₘ, or Hₐ values.  
   - Remove extreme outliers beyond the 2.5th/97.5th percentiles in key climate variables to reduce undue influence.  
4. **Categorical Encoding:**  
   - Encode `system_type` as a binary factor (`"wild"` vs. `"agricultural"`).  
   - Encode `pathogen_category` (virus, bacteria, fungal parasite, insect pest, etc.) as a factor.  
   - Encode `transmission_mode` (vector‐borne vs. direct) if available.  
5. **Data Splitting:**  
   - Partition into two subsets:  
     - **Wild dataset** (n ≈ 600 observations)  
     - **Agricultural dataset** (n ≈ 3,700 observations)

---

### Statistical Modeling
All modeling lives in `notebooks/01_modeling.ipynb`.

1. **Model Structure (per System & per Climate Variable):**  
   - **Response:** `cbind(n_infected, n_total − n_infected)` with a binomial‐logit link.  
   - **Random Effects:**  
     - `(1 | study_id)` – groups multiple surveys from the same publication.  
     - `(1 | host_order)` – accounts for phylogenetic non-independence among host taxa.  
   - **Fixed Effects (Temperature Suite):**  
     - `Wᵀ` (mean survey temperature)  
     - `Hₘᵀ` (historical monthly temperature)  
     - `Hₐᵀ` (historical annual temperature)  
     - `Aᵀ` (temperature anomaly)  
     - `Aᵀ²` (quadratic anomaly)  
     - Interaction: `Hₘᵀ × Aᵀ` (thermal mismatch test)
   - **Fixed Effects (Precipitation Suite):**  
     - Analogous terms: `Wᵖ`, `Hₘᵖ`, `Hₐᵖ`, `Aᵖ`, `Aᵖ²`, `Hₘᵖ × Aᵖ`.
2. **Candidate Model Definitions:**  
   - **Model 1 (Null):** `~ pathogen_category + (1 | study_id) + (1 | host_order)`  
   - **Model 2:** `~ W + A + Hₐ`  
   - **Model 3 (Mismatch):** `~ Hₘ + A + Hₐ + Hₘ:A`  
   - **Model 4:** `~ W + A + Hₐ + I(A^2)`  
   - **Model 5:** `~ W + A + Hₘ + I(A^2)`  
   - **… up to Model 9 (A + A²)`
3. **Model Fitting & Selection:**  
   - Fit each model with `lme4::glmer(binomial)` or `glmmTMB`.  
   - Compare via AIC; record marginal R² (fixed effects only) and conditional R² (fixed + random) using `MuMIn::r.squaredGLMM()`.  
   - Check Variance Inflation Factors (VIFs) or relative increases in SE to detect collinearity, especially between `Hₘ` and `A`.
4. **Results—Wild vs. Agricultural:**  
   - **Wild (Temperature):** Model 4 (W + A + Hₐ + A²) is best.  
     - Significant `Aᵀ` (positive) and `Aᵀ²` (negative) → peak at Aᵀ ≈ +2.7 °C.  
     - Negative effect of `Hₐᵀ` (annual climate).  
     - Slight negative `Wᵀ` once anomalies and `Hₐ` accounted.  
   - **Wild (Precipitation):** Model 3 (Hₘᵖ + Aᵖ + Hₐᵖ + Hₘᵖ:Aᵖ) is best.  
     - Inverse relationship between `Hₘᵖ` and `Aᵖ`.  
     - Dry climates: positive anomalies ↑ disease; wet climates: negative anomalies ↑ disease.  
   - **Agricultural (Temperature):** Model 3 (Hₘᵀ + Aᵀ + Hₐᵀ + Hₘᵀ:Aᵀ) selected but explains little variance.  
     - Contemporaneous `Wᵀ` shows a strong positive effect in visualization (Model 4).  
     - Historical and anomaly terms small/collinear.  
   - **Agricultural (Precipitation):** No model outperforms null meaningfully—rain anomalies do not predict disease once farms use irrigation/drainage.  
5. **Extended Hypotheses (if implemented):**  
   - **Pathogen‐Type Effects:** Fit random slopes of `Aᵀ` by `pathogen_category` (e.g., `(Aᵀ | pathogen_category)`) to estimate niche‐breadth differences.  
   - **Transmission Mode Effects:** Include fixed or random effect of `transmission_mode` × `Aᵖ` to test if vector‐borne diseases respond more strongly to precipitation anomalies.

---

### Notebook Structure
- **`notebooks/00_data_ingestion.ipynb`**  
  - Downloads and cleans raw survey CSV  
  - Geocodes missing coordinates  
  - Fetches ERA5 wind/precip via Earth Engine API  
  - Saves processed `.csv` to `data/processed/`
- **`notebooks/01_feature_engineering.ipynb`**  
  - Merges survey data with WorldClim normals  
  - Computes anomalies (Aᵀ, Aᵖ) and adds `system_type`, `pathogen_category`, `transmission_mode` labels  
  - Visualizes distributions (histograms, correlation matrices) to detect outliers
- **`notebooks/02_modeling.ipynb`**  
  - Implements the nine candidate GLMMs for temperature and precipitation, separately for wild vs. agricultural.  
  - Generates model comparison tables (AIC, R²) and selects best models.  
  - Plots marginal effects:  
    - **Figure 3a–c:** Wild temperature effects (anomaly curve, Hₐ, W slice).  
    - **Figure 3d–f:** Agricultural temperature effects.  
    - **Figure 4a–c:** Wild precipitation mismatch.  
    - **Figure 4d–f:** Agriculture precipitation (flat).  
  - Includes robustness checks (e.g., drop largest studies, re‐fit).
- **`notebooks/03_extensions.ipynb`** (optional)  
  - Tests additional hypotheses on pathogen niche breadth and transmission mode.  
  - Random‐slopes models: `(Aᵀ | pathogen_category)` and `(Aᵖ | transmission_mode)`.  
  - Summarizes effect‐size heterogeneity by pathogen group and vector vs. direct.

---

### Streamlit Dashboard (`app/streamlit_app.py`)
- **Landing Page & Sidebar:**  
  - **Project Overview (collapsible):** Leverages the layperson summary with an expander for “Technical Details.”  
  - **Filter Controls:**  
    - **System Type:** Toggle between “Wild” and “Agricultural.”  
    - **Pathogen Category:** Multi‐select (virus, bacteria, fungus, etc.).  
    - **Transmission Mode:** (Vector vs. Direct).  
    - **Climate Variable:** Dropdown: “Temperature” or “Precipitation.”  
    - **Anomaly Range Slider:** Select a window of anomalies (e.g., –5 °C to +5 °C).  
- **Main Body:**  
  - **Interactive Map:** Plot sampling sites colored by system type and sized by prevalence. Hover‐tool shows `(lat, lon, prevalence, anomaly, pathogen)`.  
  - **Prevalence vs. Anomaly Plot:**  
    - Scatter + LOESS/smooth curve, faceted by pathogen category or region.  
    - Overlay best‐fit GLMM marginal effect line from notebooks (editable via dropdown).  
  - **Model Summary Panel:**  
    - Displays the selected GLMM’s fixed‐effect coefficients, standard errors, and marginal R².  
    - Option to toggle between “Wild” and “Agricultural” model outputs.  
  - **Pathogen‐by‐Region Heatmap:**  
    - Matrix of average prevalence for each pathogen category × ecoregion (aggregate).  
    - Colored intensity indicates relative disease risk; hover for numeric values.
- **Deployment Instructions:**  
  - Mention Python dependencies (`requirements.txt` includes `streamlit`, `pandas`, `geopandas`, `plotly`, `statsmodels`, `lme4`‐equivalent).  
  - Usage:  
    ```bash
    cd app
    streamlit run streamlit_app.py
    ```  
  - Dashboard refreshes dynamically when filters change.

---

### How to Run & Reproduce
1. **Clone the Repository**  
   ```bash
   git clone https://github.com/banerjixplores/demo_plant-disease.git
   cd demo_plant-disease
