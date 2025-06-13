# Learning Outcomes Evaluation

Below is a checklist of all learning outcomes (LO1–LO11) and their associated criteria. For each criterion, I have indicated how I was able to check and demonstrate achievement in my project

---

## LO1: Apply the core principles and theories of data analytics, including statistics, probability, and basic data analysis techniques.

- [x] **1.1 Describe statistics, probability, and data analysis principles.**  
  **Evidence:**  
  - The Data Load and Inspect & ETL Preprocessing notebook discusses descriptive statistics (mean, median, quantiles) and provides summary tables and plots.

  - Clear use of probability in handling missing data and outliers is shown in the data cleaning steps.

- [x] **1.2 Illustrate the application of these core principles using relevant examples to demonstrate practical understanding and application.**  
  **Evidence:**  
  - Application of statistical principles is seen in the calculation of climate anomaly distributions, disease incidence rates, and use of correlation analysis between climate variables and plant disease outcomes, as documented in EDA Hypotheses validations and Dashboard notebooks, targeted to both technical audience and stakeholders.

---

## LO2: Apply practical skills in manipulating, analysing, and interpreting data using popular data science tools and the Python programming language.

- [x] **2.1 Utilise data analytics tools and Python to manipulate and analyse data.**  
  **Evidence:**  
  - Use of pandas for data manipulation, grouping, merging, and summarization, as seen throughout the data pipeline scripts and notebooks.
  - Analysis pipelines implemented in Python, with workflows for filtering, transforming, and aggregating data.
  - Implementation done in Modeling workflow and building Streamlit app

- [x] **2.2 Evaluate Python code and queries written.**  
  **Evidence:**  
 Python code for model building, cross-validation, and evaluation in 03_modeling_workflow.ipynb demonstrates ability to read, write, and critique code. Refactoring and improvements are visible in the commit history.

- [x] **2.3 Implement data analysis techniques, coding, and tool usage.**  
  **Evidence:**  
Implementation of data visualization (seaborn, plotly), feature engineering, model interpretation, and utility scripts (in the /scripts directory) display practical tool usage.

---

## LO3: Analyse real-world problems using data analytics methodologies.

- [x] **3.1 Conduct analysis by applying data analytics methodologies to a real-world dataset.**  
  **Evidence:**  
The project tackles the real-world problem of quantifying climate impacts on plant disease, applying regression and classification models on actual ecological survey data.

- [x] **3.2 Evaluate the problem-solving approach and solutions proposed.**  
  **Evidence:**  
Problem-solving is documented in project issues, the project summary page, and in the iterative EDA/model selection process (e.g., addressing missing values, model validation, error analysis).

- [x] **3.3 Design the approach, analysis, and problem-solving techniques used for your specific data set.**  
  **Evidence:**  
The approach is systematically designed, from initial problem statement and hypothesis framing (see README and notebooks) to analysis and final model evaluation.

---

## LO4: Demonstrate Jupyter Notebook usage for data analysis, enhanced by AI assistant.

- [x] **4.1 Integrate AI tools in data analysis tasks.**  
  **Evidence:**  
Jupyter Notebooks are used throughout, with clear code, markdown, and outputs.

ChatGPT and Copilot prompts have assisted in structured markdown in the notebook cells and commit history, showing how AI assistants aided code refinement and documentation.

- [x] **4.2 Apply generative AI solutions in storytelling with data.**  
  **Evidence:**  
Data storytelling is enhanced with markdown narratives, visual summaries, and guided cell structure, especially in the EDA and modeling notebooks

- [x] **4.3 Evaluate the data analysis, including identifying limitations and considering alternative solutions.**  
  **Evidence:**  
Limitations (e.g., missing data, limited feature set, domain transfer issues) and alternative modeling strategies are discussed in notebook markdown cells.

---

## LO5: Implement effective data management practices, covering data collection, cleaning, storage, and processing.

- [x] **5.1 Demonstrate the effectiveness of data collection, cleaning, storage, and processing techniques.**  
  **Evidence:**  
- Data pipeline scripts show reproducible steps for downloading, merging, cleaning, and storing datasets (CSV formats).

- Notebooks and scripts log each processing stage, with intermediate and final outputs stored in /data/processed/.

- [x] **5.2 Apply best practices in handling and processing data.**  
  **Evidence:**  
Best practices are demonstrated through version control, use of .gitignore, and clear directory structure for raw and processed data.

---

## LO6: Assess ethical considerations, data privacy, and governance in data analytics practices, understanding the legal and social implications of data handling.

- [x] **6.1 Examine ethical issues, data privacy, and governance in the project’s methodology.**  
  **Evidence:**  
The README.md includes a data provenance section that acknowledges open-access data use, source citation, and adherence to FAIR data principles.

- [x] **6.2 Discuss the legal and social implications of the data handling and findings.**  
  **Evidence:**  
Legal and social implications are discussed in the documentation—highlighting transparency, open science, and the societal relevance of climate–disease interactions.

---

## LO7: Design and outline independent research projects in data analytics, showing an understanding of various research methodologies.

- [x] **7.1 Organise your project effectively using best practices.**  
  **Evidence:**  
- The repository uses a structured project plan (README, Kanban/sprints in /images), with clear phases: data acquisition, processing, modeling, evaluation, and reporting. 
- Separate documentation have been added for technical and stakeholder summary
- Structured methodology has been used to organize material in the project directory, to facilitate readability and reproducibility.

- [x] **7.2 Select research methodologies applicable to the project goals.**  
  **Evidence:**  
Research methodologies include hypothesis-driven analysis, feature selection, and supervised learning—all aligned with project goals and documented in the workflow notebooks.

---

## LO8: Communicate complex data insights to both technical and non-technical audiences.

- [x] **8.1 Articulate complex data insights to technical and non-technical audiences.**  
  **Evidence:**  
The [Streamlit dashboard](https://climacrophealth-wjb9htkjbammfgqzsedk6f.streamlit.app/) and summary pages present insights accessibly to a broad audience.

- [x] **8.2 Employ visualisations and narratives to enhance user understanding.**  
  **Evidence:**  
Extensive use of interactive visualizations (Plotly), and markdown storytelling in notebooks, facilitate understanding.

- [x] **8.3 Organise documentation effectively, indicating a structured approach to information sharing.**  
  **Evidence:**  
Well-structured documentation, including project summary, detailed README, and code comments, enable both technical and layperson navigation.
---

## LO9: Identify and relate the application of data analytics across various domains.

- [x] **9.1 Explore relevant applications of data analytics in the chosen data domain, indicating a breadth of understanding and curiosity.**  
  **Evidence:**  
The project demonstrates cross-domain application: plant pathology, climate science, ecology, and data science.

- [x] **9.2 Explain how data analytics and AI can address specific challenges or opportunities.**  
  **Evidence:**  
README and project summary explain how analytics and AI help address ecological and agricultural challenges, with a view toward policy and management applications.

---

## LO10: Develop plans to implement, maintain, update, and evaluate data analytics projects, applying theoretical knowledge to practical scenarios.

- [x] **10.1 Construct a complete project plan, including implementation, maintenance, updates, and evaluation phases.**  
  **Evidence:**  
The use of version control (Git), modular code, and documented future work/maintenance in the README displays forward planning.

- [x] **10.2 Reflect on the practical challenges and considerations in executing the project.**  
  **Evidence:**  
Reflection on practical challenges, e.g., scalability, model generalizability, and user feedback for the dashboard, are discussed in closing sections of notebooks and summary documentation.

---

## LO11: Demonstrate an ability to adapt to new data analytics tools, technologies, and methodologies, showing a commitment to professional development.

- [x] **11.1 Research and experiment with the application of data analytics tools, technologies, and methodologies.**  
  **Evidence:**  
Adoption of Streamlit, Plotly, and permutation feature importance, as well as experimenting with different ML models (Random Forest, Ridge, etc.), demonstrates tool adaptability.

- [x] **11.2 Evaluate the learning process and how the project has prepared the student for continuous learning and adaptation in the field.**  
Reflections in the project documentation and commit history outline the learning curve, adoption of best practices, and intent for further upskilling in cloud deployment and ML explainability.


---
