import pandas as pd
import sqlite3

# Configuration
CSV_FILE = "sample_data/sales_sample.csv"
DB_FILE = "sales_analytics.db"

# Connect to SQLite
conn = sqlite3.connect(DB_FILE)


# Step 1: Bronze Layer - Raw Ingestion
df_raw = pd.read_csv(CSV_FILE)
df_raw.to_sql("bronze_sales", conn, if_exists="replace", index=False)
print(f"[INFO] Bronze layer written: {len(df_raw)} rows")


# Step 2: Silver Layer - Cleaning & Deduplication
df_silver = df_raw.copy()

# Standardize columns
df_silver.columns = [c.lower() for c in df_silver.columns]

# Fill nulls
df_silver['product'] = df_silver['product'].fillna('Unknown')
df_silver['quantity'] = df_silver['quantity'].fillna(0)
df_silver['revenue'] = df_silver['revenue'].fillna(0)

# Remove duplicates
df_silver = df_silver.drop_duplicates(subset=['order_id'])

# Write Silver layer
df_silver.to_sql("silver_sales", conn, if_exists="replace", index=False)
print(f"[INFO] Silver layer written: {len(df_silver)} rows")


# Step 3: Gold Layer - KPIs / Aggregations
# Revenue per product
df_revenue = df_silver.groupby('product')['revenue'].sum().reset_index()

# Top customers by revenue
df_top_customers = df_silver.groupby('customer_id')['revenue'].sum().reset_index().sort_values(by='revenue', ascending=False)

# Combine KPIs (simplified)
df_gold = pd.concat([df_revenue, df_top_customers], axis=1)

# Write Gold layer
df_gold.to_sql("gold_sales_kpis", conn, if_exists="replace", index=False)
print(f"[INFO] Gold layer written: {len(df_gold)} rows")

conn.close()
print("[INFO] ETL pipeline completed successfully!")
