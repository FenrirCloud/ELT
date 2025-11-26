# ELT Project with Python, DuckDB, dbt, and Streamlit

This project is a complete, step-by-step tutorial for building a modern, open-source ELT (Extract, Load, Transform) pipeline. It uses the Olist Brazilian E-Commerce dataset to demonstrate how to ingest, model, and visualize data.

## 🚀 Technology Stack

- **Python**: For scripting the data loading process.
- **DuckDB**: As the analytical database. It's fast, serverless, and integrates well with Python.
- **dbt Core**: For transforming data using SQL-based models.
- **GitHub Actions**: For orchestrating the pipeline and running it on a schedule.
- **Streamlit**: For building a simple and interactive data dashboard.

## 📂 Project Structure

```
elt_project/
│
├── .github/
│   └── workflows/
│       └── run_elt_pipeline.yml  -- GitHub Actions workflow
│
├── data/
│   └── ecommerce.duckdb          -- DuckDB database file
│   └── *.csv                     -- Raw data files (after download)
│
├── dbt_project/
│   ├── models/
│   │   ├── staging/              -- Staging models for cleaning data
│   │   │   ├── stg_customers.sql
│   │   │   ├── stg_order_items.sql
│   │   │   └── stg_orders.sql
│   │   └── facts/                -- Fact models for business logic
│   │       └── fct_orders.sql
│   ├── dbt_project.yml           -- dbt project configuration
│   └── ...
│
├── scripts/
│   ├── load_data.py              -- Python script to load CSVs into DuckDB
│   └── inspect_db.py             -- Helper script to inspect database schema
│
├── streamlit_app/
│   └── app.py                    -- Streamlit dashboard application
│
├── profiles.yml                  -- dbt profile configuration
└── README.md                     -- This file
```

## ⚙️ How to Run

### 1. Prerequisites

- Python 3.9+
- Pip (Python package installer)

### 2. Installation

Clone the repository and install the required Python packages:

```bash
git clone <your-repo-url>
cd elt_project
pip install -r requirements.txt 
```
*(Note: You will need to create a `requirements.txt` file. You can generate one with `pip freeze > requirements.txt` after installing the packages manually as we did in the tutorial)*

### 3. Run the ELT Pipeline Manually

1.  **Load Data**: Run the Python script to download the dataset and load it into DuckDB.
    ```bash
    python scripts/load_data.py
    ```

2.  **Transform Data**: Run the dbt models to transform the raw data into analytical tables.
    ```bash
    dbt run --project-dir dbt_project --profiles-dir .
    ```

### 4. Run the Streamlit Dashboard

To view the dashboard, run the Streamlit application:

```bash
streamlit run streamlit_app/app.py
```

## 🤖 Automation with GitHub Actions

The pipeline is configured to run automatically every day from Monday to Friday at midnight UTC. This is defined in the `.github/workflows/run_elt_pipeline.yml` file. You can also trigger it manually from the "Actions" tab in your GitHub repository.
