-- gold_transform.sql
-- Gold Layer: aggregated KPIs

-- Revenue per product
CREATE OR REPLACE TABLE gold_revenue_per_product AS
SELECT
    product,
    SUM(revenue) AS total_revenue
FROM silver_sales
GROUP BY product;

-- Top customers by revenue
CREATE OR REPLACE TABLE gold_top_customers AS
SELECT
    customer_id,
    SUM(revenue) AS total_revenue
FROM silver_sales
GROUP BY customer_id
ORDER BY total_revenue DESC;
