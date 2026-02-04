-- silver_transform.sql
-- Silver Layer: cleaning & deduplication

CREATE OR REPLACE TABLE silver_sales AS
SELECT DISTINCT
    LOWER(order_id) AS order_id,
    LOWER(customer_id) AS customer_id,
    LOWER(product) AS product,
    COALESCE(quantity, 0) AS quantity,
    COALESCE(revenue, 0) AS revenue,
    order_date
FROM bronze_sales
WHERE order_id IS NOT NULL;
