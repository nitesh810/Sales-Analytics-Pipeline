-- bronze_transform.sql
-- Bronze Layer: raw ingestion (store as it is)

CREATE OR REPLACE TABLE bronze_sales AS
SELECT *
FROM staging_sales;
