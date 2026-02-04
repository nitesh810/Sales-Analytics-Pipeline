# Sales Analytics Pipeline

## Project Overview
This project demonstrates a **Python ETL pipeline using PySpark** to process sales CSV data, clean, transform, and generate **analytics-ready datasets**. The pipeline follows a **Bronze → Silver → Gold** architecture.

- **Bronze Layer:** Raw ingestion of sales CSV data.
- **Silver Layer:** Data cleaning, deduplication, and standardization.
- **Gold Layer:** Aggregations to compute KPIs such as revenue per product and top customers by revenue.

## Technology Stack
- **Languages:** Python, PySpark, SQL
- **Databases:** SQLite
- **Tools:** Git/GitHub
- **Data Format:** CSV

## ETL Pipeline Flow

```
    Sales CSV
        │
        ▼
  Python ETL Job (PySpark)
        │
        ├─> Bronze Layer (raw ingestion)
        │     - Read CSV using Spark
        │     - Write raw data to Bronze table / folder
        │
        ├─> Silver Layer (cleaning & deduplication)
        │     - Standardize columns (lowercase)
        │     - Fill nulls for product, quantity, revenue
        │     - Remove duplicates by order_id
        │     - Write clean data to Silver table / folder
        │
        └─> Gold Layer (aggregations / KPIs)
              - Compute revenue per product
              - Compute profit margin trends
              - Write analytics-ready table for reporting
```

## Sample Data
- `sample_data/sales_sample.csv` contains sample orders for testing the pipeline.

## Key Features
- **Bronze → Silver → Gold architecture** for ETL best practices.
- **Data quality checks**: duplicates removed, missing values filled.
- **KPI generation**: Revenue trends, top customers.
- **Scalable PySpark implementation**, ready for larger datasets.
- Awareness of **cloud migration** and streaming pipelines (e.g., Pub/Sub or Dataflow) for future improvements.

## Steps to Run
1. Install PySpark: `pip install pyspark`
2. Navigate to the project folder
3. Run the ETL job:
```bash
python etl_jobs/sales_etl.py
4. Output CSVs will be generated in output/bronze_sales, output/silver_sales, and output/gold_*.

## Repository Structure

```bash
sales_analytics_pipeline/
│
├── etl_jobs/
│   └── sales_etl.py    # Python ETL job for Bronze → Silver → Gold transformations
│
├── sql_transformations/
│   ├── bronze_transform.sql   # Bronze layer raw ingestion transformations
│   ├── silver_transform.sql   # Silver layer cleaning/dedup transformations
│   └── gold_transform.sql     # Gold layer KPI/reporting transformations
│
├── sample_data/
│   └── sales_sample.csv       # Sample sales CSV to test pipeline
│
└── README.md                  # Project description, architecture, data flow, KPIs
```
___
