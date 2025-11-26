# Olist E-Commerce ELT Pipeline

This project demonstrates a simple, open-source ELT pipeline using the Olist Brazilian E-Commerce dataset.

### Tech Stack
*   **Extract & Load**: Python & DuckDB
*   **Transform**: dbt Core
*   **Orchestration**: GitHub Actions
*   **Dashboard**: Streamlit

---

### How to Run

**1. Prerequisites:**
*   Python 3.9+

**2. Setup:**

Clone the repo and install dependencies.
```bash
git clone https://github.com/FenrirCloud/ELT.git
cd ELT
pip install -r requirements.txt
```

**3. Run Pipeline:**

First, load the raw data into DuckDB.
```bash
python elt_project/scripts/load_data.py
```

Next, run the dbt transformations.
```bash
dbt run --project-dir elt_project/dbt_project --profiles-dir elt_project
```

**4. View Dashboard:**

Launch the Streamlit app to see the results.
```bash
streamlit run elt_project/streamlit_app/app.py
```

---

### Automation

A GitHub Actions workflow is included in `.github/workflows` to run the pipeline on a schedule (Mon-Fri at midnight UTC) or manually.