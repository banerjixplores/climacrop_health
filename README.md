# 🍃 ClimaCrop Health: Plant Disease & Climate Impact Analysis

**ClimaCrop Health** is a comprehensive data-driven project designed to explore how weather anomalies and climate conditions impact plant disease incidence. Building on research from Kirk et al. (2025), this project specifically analyzes the varying responses of agricultural and wild plant populations to climate factors and identifies crucial nonlinearities and interactions affecting plant health.

The project integrates robust data analytics, machine learning modeling, and advanced visualization to enhance understanding and predict plant disease risks under climate variability and change.

<p align="center">
  <img src="images/plant_disease.gif" alt="Climate Impact Animation" width="1000"/>
</p>

**Table of Contents**
- [🍃 ClimaCrop Health: Plant Disease \& Climate Impact Analysis](#-climacrop-health-plant-disease--climate-impact-analysis)
  - [Dataset Content](#dataset-content)
  - [Getting Started](#getting-started)
  - [Project Objectives](#project-objectives)
  - [Business Requirements](#business-requirements)
  - [Hypothesis and how to validate?](#hypothesis-and-how-to-validate)
      - [1. Data \& Anomalies](#1-data--anomalies)
      - [2. Statistical Approach](#2-statistical-approach)
        - [Temperature](#temperature)
        - [Rainfall](#rainfall)
  - [Project Plan](#project-plan)
  - [The rationale to map the business requirements to the Data Visualisations](#the-rationale-to-map-the-business-requirements-to-the-data-visualisations)
  - [Analysis techniques used](#analysis-techniques-used)
  - [Ethical considerations](#ethical-considerations)
  - [Dashboard Design](#dashboard-design)
  - [Unfixed Bugs](#unfixed-bugs)
  - [Development Roadmap](#development-roadmap)
  - [Deployment](#deployment)
    - [Heroku](#heroku)
  - [Main Data Analysis Libraries](#main-data-analysis-libraries)
  - [Notebook contents](#notebook-contents)
  - [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
  - [Acknowledgements](#acknowledgements)

## Dataset Content

- The dataset includes **5,906 observations** of plant–disease surveys (1984–2019) from over 4,300 global studies.
- Paired with ERA5‐land (monthly) and WorldClim 30-year normals.
- Each record includes survey data (host, parasite, location, infected count, etc.) and associated climate metrics (e.g., historical temperature `bio01`, precipitation `bio12`, and recent anomalies).
- Dataset source: [Dryad Repository – DOI 10.5061/dryad.p8cz8wb0h](https://doi.org/10.5061/dryad.p8cz8wb0h)

## Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/banerjixplores/climacrop_health.git
   ```
2. Navigate to the project directory:
   ```bash
   cd climacrop_health
   ```
3. Create & activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
4. Install the required packages:
   ```bash      
   pip install -r requirements.txt
   ```
5. Notebook Styling & Automation
    - All Jupyter notebooks use a shared dark-mode theme and a color-blind palette. When you open any notebook, the 00_notebook_style.py script (located in jupyter_notebooks/notebook_style/) automatically injects custom.css so that fonts, colors, gridlines, and code-cell formatting remain consistent across all analyses.
    - As soon as you open any notebook, the styling script will inject custom.css so that fonts, colors, and code‐cell borders remain consistent.
    - Dark-mode CSS: jupyter_notebooks/notebook_style/custom.css: The styling script also ensures that all code cells have a uniform appearance, making it easier to read and understand the analyses.
    - Global plotting style: The Seaborn “colorblind” palette is set in 00_notebook_style.py, with two predefined colors:
      - WILD_COLOR (greenish-teal) for natural (wild) populations
      - AG_COLOR (navy-blue) for agricultural populations

6. Notebook execution:
   - Open Jupyter Notebook or your preferred IDE.
   - Run the notebooks in sequence starting from `00_data_load_and_inspect.ipynb` to ensure data is loaded and processed correctly.
     - jupyter_notebooks/00_data_load_and_inspect.ipynb
     - jupyter_notebooks/01_etl_preprocessing.ipynb
     - jupyter_notebooks/02_eda.ipynb
     - ... continue with the remaining notebooks in order.
7. Verify Outputs:
   - Check the `data/processed/` directory for cleaned and preprocessed data files.
   - Review generated visualizations in the EDA notebook.
   - 

## Project Objectives

- Predict and classify disease incidence based on climate inputs
- Identify which climate metrics (historic vs. anomalous) drive disease prevalence
- Compare sensitivity between natural and agricultural systems
- Deploy an interactive Streamlit dashboard for risk visualization and scenario testing
- Ensure the approach is explainable and reproducible for real-world use


## Business Requirements

- **Enable risk forecasting** based on temperature and rainfall inputs.
- **Provide incidence classification** across zones for easy interpretability.
- **Highlight hotspots** on a global scale to prioritize surveillance.
- **Facilitate exploratory scenario simulation** for stakeholders via an interactive interface.


## Hypothesis and how to validate?

- ### **Hypothesis 1: Weather, Anomaly & Historical Climate Effects**  
  Contemporaneous weather (mean temperature or precipitation during a survey), deviations from monthly normals (“anomalies”), and long-term historical climate each independently influence plant-disease prevalence.

- ### **Hypothesis 1 validation**

**Weather (contemporaneous), anomalies, and historical climate each influence disease prevalence.**

| Predictor                         | System | R²     | Adj. R² | p(linear) | p(quad) | Interpretation                         |
| --------------------------------- | ------ | ------ | ------- | --------- | ------- | -------------------------------------- |
| **Temperature Anomaly**           | Wild   | 0.0687 | 0.0653  | 4.3e-10   | 7.9e-02 | Linear sig., quad not; \~6.9% variance |
|                                   | Ag     | 0.0071 | 0.0065  | 1.3e-06   | 1.1e-03 | Both terms sig.; \~0.7% variance       |
| **Contemp. Temperature**          | Wild   | 0.0740 | 0.0706  | 1.6e-09   | 3.7e-10 | Both terms sig.; \~7.4% variance       |
|                                   | Ag     | 0.0698 | 0.0693  | 4.5e-17   | 3.8e-23 | Both terms sig.; \~7.0% variance       |
| **Historical Annual Temperature** | Wild   | 0.1153 | 0.1120  | 9.6e-14   | 1.7e-11 | Both terms sig.; \~11.5% variance      |
|                                   | Ag     | 0.0359 | 0.0353  | 7.2e-21   | 1.1e-24 | Both terms sig.; \~3.6% variance       |

Conclusion:

- All three temperature metrics explain more variance in wild than agricultural systems.
  
**Rainfall (anomaly, contemporary, monthly & annual) affects disease more strongly in wild than in agricultural systems.**

| Predictor                          | System | R²     | Adj. R² | p(linear) | p(quad) | Interpretation                         |
| ---------------------------------- | ------ | ------ | ------- | --------- | ------- | -------------------------------------- |
| **Rainfall Anomaly**               | Wild   | 0.0134 | 0.0098  | 6.6e-03   | 1.0e-02 | Both terms significant; \~1.3% variance       |
|                                    | Ag     | 0.0590 | 0.0585  | 8.5e-02   | 3.8e-06 | Quad significant, linear not; \~5.9% variance |
| **Contemp. Precipitation (mm/d)**  | Wild   | 0.0365 | 0.0329  | 2.0e-05   | 6.4e-06 | Both terms significant; \~3.6% variance       |
|                                    | Ag     | 0.0242 | 0.0237  | 7.5e-07   | 6.8e-02 | Linear significant, quad not; \~2.4% variance |
| **Monthly Historical Rain (mm/d)** | Wild   | 0.0134 | 0.0098  | 6.7e-03   | 1.0e-02 | Both terms significant; \~1.3% variance       |
|                                    | Ag     | 0.0590 | 0.0585  | 8.6e-02   | 3.7e-06 | Quad significant, linear not; \~5.9% variance |
| **Annual Precipitation (mm/d)**    | Wild   | 0.0089 | 0.0053  | 2.8e-02   | 2.8e-02 | Both terms significant; \~0.9% variance       |
|                                    | Ag     | 0.0313 | 0.0307  | 2.9e-04   | 3.9e-08 | Both terms significant; \~3.1% variance       |

Conclusion:

- Only Contemporary Precipitation shows a stronger effect in Wild (R² 0.0365 > 0.0242).

- For Rainfall Anomaly, Monthly Historical, and Annual precipitation, Agricultural explains equal or more variance than Wild.

- Thus, rainfall does not universally follow the same Wild > Ag pattern — it is a more system-specific driver.

---

- ### **Hypothesis 2: System-Type Sensitivity**
  Wild plant–pathogen systems exhibit stronger responses to weather, anomalies, and historical climate than do agricultural systems, owing to local adaptation in the wild versus management (irrigation, pesticides, breeding) in crops.
- ### **Hypothesis 2 validation**

| System | Metric             | Temp Wild R² | Temp Ag R² | Rain Wild R² | Rain Ag R² | Wild > Ag? |
| ------ | ------------------ | ------------ | ---------- | ------------ | ---------- | ---------- |
| Temp   | Annual Historical  | 0.1153       | 0.0359     | –            | –          | yes        |
| Temp   | Anomaly            | 0.0687       | 0.0071     | –            | –          | yes        |
| Temp   | Contemporary       | 0.0740       | 0.0698     | –            | –          | slightly   |
| Rain   | Annual Historical  | –            | –          | 0.0089       | 0.0313     | no         |
| Rain   | Anomaly            | –            | –          | 0.0134       | 0.0590     | no         |
| Rain   | Contemporary       | –            | –          | 0.0365       | 0.0242     | yes        |
| Rain   | Monthly Historical | –            | –          | 0.0134       | 0.0590     | no         |

**1. Temperature:**

- Wild systems consistently show higher R² than agricultural for all three temperature metrics (annual historical, anomaly, contemporary).

- **Conclusion: Wild plant–pathogen systems are indeed more sensitive to temperature effects → Hypothesis 2 validated for temperature.**

**2. Rainfall:**

- Only contemporary precipitation yields slightly higher Wild R² (0.0365 vs. 0.0242).

- All other rainfall metrics (anomaly, annual & monthly historical) are stronger in agricultural systems.

- **Conclusion: Hypothesis 2 is not upheld for precipitation → rainfall-driven disease variation does not show uniformly greater sensitivity in wild systems.**

---

- ### **Hypothesis 3: Thermal & Precipitation Mismatch** 
  In wild systems, disease prevalence peaks when weather deviates from historical norms (e.g., unusually warm in a cool climate or vice versa)—a “mismatch” effect. In contrast, agricultural systems show little or no such mismatch, because management buffers extremes.

- ### **Hypothesis 3 validation**
We tested Hypothesis 3: Thermal & Precipitation Mismatch by fitting OLS models with interaction terms between anomaly and historical climate for both wild and agricultural systems.

#### 1. Data & Anomalies

- Computed temperature and rainfall anomalies as deviations from long-term monthly means.

- Took absolute values to capture “mismatch magnitude.”

#### 2. Statistical Approach
- Separate OLS regressions for Wild vs. Ag:

##### Temperature
```python
import statsmodels.formula.api as smf

# e.g. for wild_df or ag_df
model = smf.ols(
    formula='incidence ~ temp_anomaly_C * monthly_temp_C',
    data=system_df
).fit()
print(model.summary())
```

##### Rainfall
```python
model = smf.ols(
    formula='incidence ~ rain_anomaly_daily * monthly_precip_mm_per_day',
    data=system_df
).fit()
print(model.summary())
```

- Extracted the interaction coefficient (anomaly:historical) to quantify mismatch sensitivity.

3. Key Interaction Coefficients
   
|         Effect        | Wild Coef. | Ag Coef. |   p-value   |
| :-------------------: | ---------: | -------: | :---------: |
| **Temp × Historical** |    –0.0142 |  –0.0031 | **< 0.001** |
| **Rain × Historical** |    –0.0312 |  –0.0069 |   *< 0.01*  |

   - **Interpretation**: Wild systems show significant negative interaction effects for both temperature and rainfall anomalies with historical norms, indicating stronger mismatch sensitivity. Agricultural systems have weaker or no significant interactions.
   - **Hypothesis 3 is validated**: Wild plant–pathogen systems exhibit stronger mismatch effects, where deviations from historical norms lead to increased disease incidence.

- **Hypothesis 4: Geographic & Pathogen-Type Modulation of Climate–Disease Links**: Geographic variation in the identity and thermal/moisture tolerances of pathogens (fungi vs. bacteria vs. viruses vs. nematodes, etc.) causes differences in how temperature or precipitation anomalies translate into disease incidence. Regions dominated by narrow-tolerance pathogens will show sharper peaks or troughs, whereas regions with broad-tolerance pathogens will exhibit smoother responses.
- **Hypothesis 5: Transmission-Mode Sensitivity to Anomalies**: Pathogens spread by vectors (insects or mites) will exhibit stronger sensitivity to precipitation anomalies (e.g., drought or heavy rain) than directly transmitted (e.g., soil-borne or contact) pathogens, because vector activity and life cycles respond acutely to moisture conditions.

Validation Strategy:
- Correlation analysis between `incidence` and climate metrics.
- Comparison of means using visual plots (e.g., KDE, boxplot) across system types.
- Stratified accuracy testing using Random Forest classifiers.

## Project Plan
* Outline the high-level steps taken for the analysis.
* How was the data managed throughout the collection, processing, analysis and interpretation steps?
* Why did you choose the research methodologies you used?

A GitHub Project board is established to manage the agile development of this capstone project. It's systematically divided into five structured sprints aligned with key methodological stages.

**GitHub Project Board:** [ClimaCrop Kanban Project](https://github.com/users/banerjixplores/projects/6/views/1)

**Sprint 1 - Day 1:**  
<img src="images/Kanban_sprint_1_init.png" alt="Sprint 1 Start" width="45%" style="float: left; margin-right: 5%;" />
<img src="images/Kanban_sprint_1_end.png"  alt="Sprint 1 End"   width="45%" style="float: right; margin-left: 5%;" />
<img src="images/Kanban_sprint_2_init.png" alt="Sprint 2 Start" width="45%" style="float: left; margin-right: 5%;" />

<div style="clear: both;"></div>


**Sprint Breakdown & Detailed Tasks**

**Sprint 1: Data Acquisition, Inspection & Preprocessing**

**1.1 Data Acquisition**
- Load and examine the `merged_climate_disease_final.csv` dataset (Dryad/Kirk et al. 2025).
- Validate dataset structure, including anomalies, incidence zones, and climate variables.
- Document data provenance and initial understanding context.

**1.2 Data Quality Checks**
- Detect and manage duplicated entries.
- Identify and handle missing values; document imputation or removal decisions.
- Validate column encodings against Kirk et al.’s original dataset features.

**1.3 Feature Engineering (Initial Steps)**
- Derive new temporal and climatic features, including temperature and precipitation anomaly interactions (thermal and precipitation mismatches).
- Normalize and encode categorical variables (`host_type`, `habitat`).
- Save preprocessed dataset to `data/processed/`.


**Sprint 2: Exploratory Data Analysis & Hypothesis Validation**

**2.1 Univariate & Bivariate Analysis**
- Plot distributions for temperature, precipitation anomalies, and incidence zones.
- Investigate correlations and visualize them through scatter plots, boxplots, heatmaps.

**2.2 Hypothesis-Driven Statistical Testing**
Evaluate Kirk et al.’s hypotheses:
- Weather & climate predict disease prevalence.
- Thermal and precipitation mismatch effects.
- Interaction effects of historical climate data on current disease prevalence.

**Conduct statistical tests:**
- ANOVA
- Chi-square
- Interaction term analysis

**2.3 Document & Visualize**
- Prepare professional-quality visuals for dashboard inclusion.
- Summarize EDA findings clearly for subsequent modeling steps.


**Sprint 3: Predictive Modeling & Evaluation**

**3.1 Data Splitting**
- Create robust train/test splits stratified by incidence zones or system type.

**3.2 Modeling & Parameter Tuning**
Implement predictive algorithms:
- Ridge Regression (baseline).
- Random Forest (interpretable non-linear model).
- XGBoost (optimized gradient boosting).

- Conduct hyperparameter tuning using GridSearchCV.

**3.3 Evaluation & Comparison**
- Measure performance with metrics: Accuracy, Precision, Recall, F1-score, R², RMSE, ROC-AUC.
- Analyze results separately for agricultural vs. wild systems.
- Save best-performing models and evaluation metrics.


**Sprint 4: Explainability & Interactive Dashboard Development**

**4.1 Model Explainability**
- Generate Permutation Importance plots.
- Create Partial Dependence Plots (PDP) to elucidate feature influences.

**4.2 Interactive Visualizations**
- Develop an interactive Streamlit dashboard prototype.
- Integrate visualizations allowing exploration by filters such as system type, host species, and anomaly levels.

**4.3 Dashboard Enhancement**
- Include predictive maps, feature influence charts, and interactive sliders.
- Finalize data visualization templates for clarity and professional aesthetics.


**Sprint 5: Reporting, Documentation, and Final Delivery**

**5.1 Documentation**
- Polish final README.md for clarity, professionalism, and completeness.
- Write comprehensive yet accessible technical and lay summaries.

**5.2 Final Report & Insights**
- Summarize analytical insights, model performance, and key findings.
- Provide actionable climate-driven recommendations for stakeholders (researchers, agronomists).

**5.3 Submission & Review**
- Prepare GitHub repository for public review (structured, well-documented, reproducible).
- Record optional walkthrough for stakeholders.
- Tag and release final GitHub repository version (`v1.0-climacrop-capstone`).


**Ethical & Scientific Considerations**

**Transparency & Reproducibility**
- Fully document all analytical decisions for transparency.
- Provide clear and comprehensive notes within notebooks and markdown files.

**Bias Mitigation**
- Identify and acknowledge potential geographical biases and system-type coverage discrepancies.
- Include clear discussions on how these biases were mitigated through analysis and interpretation strategies.

**Data Privacy & Compliance**
- Confirm the dataset does not contain identifiable sensitive information (compliant with ethical standards).


## The rationale to map the business requirements to the Data Visualisations
* List your business requirements and a rationale to map them to the Data Visualisations

## Analysis techniques used

- **Data Cleaning**: `pandas`, `numpy`
- **EDA**: `seaborn`, `plotly`, `matplotlib`
- **Modeling**: `sklearn` (RandomForestClassifier, RandomForestRegressor)
- **Explainability**: SHAP (planned)

**Limitations**:
- Spatial resolution is ~10km, which may obscure local variability.
- Missing metadata for some studies.

**Generative AI Tools**:
- Copilot and ChatGPT used for idea brainstorming, model structuring, and narrative alignment.

## Ethical considerations
* Were there any data privacy, bias or fairness issues with the data?
* How did you overcome any legal or societal issues?

## Dashboard Design
* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other item that your dashboard library supports.
* Later, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project you were confident you would use a given plot to display an insight but subsequently you used another plot type).
* How were data insights communicated to technical and non-technical audiences?
* Explain how the dashboard was designed to communicate complex data insights to different audiences. 

## Unfixed Bugs
* Please mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable to consider, paucity of time and difficulty understanding implementation are not valid reasons to leave bugs unfixed.
* Did you recognise gaps in your knowledge, and how did you address them?
* If applicable, include evidence of feedback received (from peers or instructors) and how it improved your approach or understanding.

## Development Roadmap
* What challenges did you face, and what strategies were used to overcome these challenges?
* What new skills or tools do you plan to learn next based on your project experience? 

| Phase | Description |
|-------|-------------|
| Data Understanding | Clean, merge, validate, and profile datasets |
| Feature Engineering | Engineer `incidence_zone`, climate anomalies, study metadata |
| Modeling | Train classification & regression models; validate performance |
| Dashboard | Build Streamlit app with sliders, KPI cards, and prediction interface |
| Explainability | Use SHAP to visualize feature importance |
| Deployment & Docs | Finalize README, deploy dashboard, and document pipeline

## Deployment
### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. From the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.


## Main Data Analysis Libraries
* Here you should list the libraries you used in the project and provide an example(s) of how you used these libraries.

```bash
pandas, numpy, seaborn, plotly, matplotlib, scikit-learn, joblib, streamlit
```


## Notebook contents
| Notebook                           | Inputs                                                                             | Outputs                                                                        |
| ---------------------------------- | ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| 00\_data\_load\_and\_inspect.ipynb | `data/raw/merged_climate_disease_final.csv`, Python packages (Pandas, NumPy, etc.) | DataFrame inspection, initial distribution plots, optional `raw_inspected.csv` |
| 01\_etl\_preprocessing.ipynb       | `data/raw/merged_climate_disease_final.csv` (or `raw_inspected.csv`)               | `data/processed/cleaned_climate_disease.csv`, engineered features              |
…                                                                             |



## Credits 

* In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- Primary dataset and paper: Kirk et al. (2024), Ecology Letters
- Data source: [https://datadryad.org/stash/dataset/doi:10.5061/dryad.p8cz8wb0h](https://datadryad.org/stash/dataset/doi:10.5061/dryad.p8cz8wb0h)
- Method inspiration: Code Institute bootcamp resources

### Media

- The photos used on the home and sign-up page are from This Open-Source site
- The images used for the gallery page were taken from this other open-source site



## Acknowledgements 
- Mentors and reviewers at Code Institute
- Code Institute Slack peer feedback group

<p align="center">
  <img src="images/plant_health_logo.jpg" alt="Plant Health Footer Logo" width="120"/>
</p>
