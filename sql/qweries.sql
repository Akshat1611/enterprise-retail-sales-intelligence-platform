
-- Query 1 : Total Revenue
-- Business Question:
-- How much total revenue has the company generated?


SELECT
    SUM(sales_amount) AS total_revenue
FROM fact_sales;

-- Query 2 : Total Profit
-- Business Question:
-- How much total profit has the company earned?

SELECT
    SUM(profit) AS total_profit
FROM fact_sales;


-- Query 3 : Total Orders
-- Business Question:
-- How many orders were placed?


SELECT
    COUNT(*) AS total_orders
FROM fact_sales;

-- Query 4 : Average Order Value
-- Business Question:
-- What is the average revenue generated per order?


SELECT
    ROUND(AVG(sales_amount),2) AS average_order_value
FROM fact_sales;

-- Query 5 : Sales by Category
-- Business Question:
-- Which product category generates the highest sales?


SELECT
    p.category,
    SUM(f.sales_amount) AS total_sales
FROM fact_sales f
JOIN dim_product p
ON f.product_id = p.product_id
GROUP BY p.category
ORDER BY total_sales DESC;

-- Query 6 : Profit by Category
-- Business Question:
-- Which category is the most profitable?


SELECT
    p.category,
    SUM(f.profit) AS total_profit
FROM fact_sales f
JOIN dim_product p
ON f.product_id = p.product_id
GROUP BY p.category
ORDER BY total_profit DESC;

-- Query 7 : Top 10 Products by Revenue
-- Business Question:
-- Which products generate the highest revenue?


SELECT
    p.product_name,
    SUM(f.sales_amount) AS revenue
FROM fact_sales f
JOIN dim_product p
ON f.product_id = p.product_id
GROUP BY p.product_name
ORDER BY revenue DESC
LIMIT 10;

-- Query 8 : Top 10 Customers
-- Business Question:
-- Which customers contribute the most revenue?


SELECT
    c.customer_name,
    SUM(f.sales_amount) AS revenue
FROM fact_sales f
JOIN dim_customer c
ON f.customer_id = c.customer_id
GROUP BY c.customer_name
ORDER BY revenue DESC
LIMIT 10;

-- Query 9 : Sales by Store
-- Business Question:
-- Which stores perform the best?

SELECT
    s.store_name,
    SUM(f.sales_amount) AS total_sales
FROM fact_sales f
JOIN dim_store s
ON f.store_id = s.store_id
GROUP BY s.store_name
ORDER BY total_sales DESC;


-- Query 10 : Monthly Sales Trend
-- Business Question:
-- How does revenue change month over month?


SELECT
    d.year,
    d.month_name,
    SUM(f.sales_amount) AS revenue
FROM fact_sales f
JOIN dim_date d
ON f.date_id = d.date_id
GROUP BY
    d.year,
    d.month,
    d.month_name
ORDER BY
    d.year,
    d.month;


-- Query 11 : Payment Method Analysis
-- Business Question:
-- Which payment methods are used the most?

SELECT
    payment_method,
    COUNT(*) AS total_orders,
    SUM(sales_amount) AS revenue
FROM fact_sales
GROUP BY payment_method
ORDER BY revenue DESC;

-- Query 12 : Order Status Analysis
-- Business Question:
-- How many orders are completed, returned, or cancelled?


SELECT
    order_status,
    COUNT(*) AS total_orders,
    SUM(sales_amount) AS revenue
FROM fact_sales
GROUP BY order_status
ORDER BY revenue DESC;


-- Query 13 : Top 5 Stores in Each Region
-- Business Question:
-- Which stores perform best within every region?

SELECT *
FROM (
    SELECT
        s.region,
        s.store_name,
        SUM(f.sales_amount) AS revenue,
        RANK() OVER(
            PARTITION BY s.region
            ORDER BY SUM(f.sales_amount) DESC
        ) AS rank
    FROM fact_sales f
    JOIN dim_store s
    ON f.store_id = s.store_id
    GROUP BY
        s.region,
        s.store_name
) ranked_stores
WHERE rank <= 5;

-- Query 14 : Running Revenue
-- Business Question:
-- What is the cumulative revenue over time?

SELECT
    d.full_date,
    SUM(f.sales_amount) AS daily_sales,
    SUM(SUM(f.sales_amount))
    OVER(
        ORDER BY d.full_date
    ) AS running_revenue
FROM fact_sales f
JOIN dim_date d
ON f.date_id = d.date_id
GROUP BY d.full_date
ORDER BY d.full_date;


-- Query 15 : Customer Lifetime Value (CLV)
-- Business Question:
-- Which customers have generated the highest lifetime revenue?


WITH customer_sales AS (

    SELECT
        c.customer_id,
        c.customer_name,
        SUM(f.sales_amount) AS lifetime_value
    FROM fact_sales f
    JOIN dim_customer c
    ON f.customer_id = c.customer_id
    GROUP BY
        c.customer_id,
        c.customer_name
)
SELECT *
FROM customer_sales
ORDER BY lifetime_value DESC
LIMIT 10;