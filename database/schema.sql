
-- Enterprise Retail Sales Intelligence Platform
-- Database Schema
-- PostgreSQL 18
-- Author: Akshat Sharma

-- Drop Existing Tables (Safe for Development)

DROP TABLE IF EXISTS fact_sales CASCADE;
DROP TABLE IF EXISTS dim_customer CASCADE;
DROP TABLE IF EXISTS dim_product CASCADE;
DROP TABLE IF EXISTS dim_store CASCADE;
DROP TABLE IF EXISTS dim_promotion CASCADE;
DROP TABLE IF EXISTS dim_date CASCADE;


-- Customer Dimension

CREATE TABLE dim_customer (

    customer_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    customer_name VARCHAR(100) NOT NULL,

    gender VARCHAR(10)
        CHECK (gender IN ('Male', 'Female', 'Other')),

    age INT
        CHECK (age BETWEEN 18 AND 100),

    city VARCHAR(100),

    state VARCHAR(100),

    country VARCHAR(100),

    income DECIMAL(12,2)
        CHECK (income >= 0),

    customer_segment VARCHAR(30)
        CHECK (
            customer_segment IN (
                'Regular',
                'Premium',
                'VIP'
            )
        ),

    join_date DATE

);


-- Product Dimension

CREATE TABLE dim_product (

    product_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    product_name VARCHAR(150) NOT NULL,

    category VARCHAR(50) NOT NULL,

    sub_category VARCHAR(50),

    brand VARCHAR(50),

    supplier VARCHAR(100),

    cost_price DECIMAL(12,2)
        CHECK (cost_price >= 0),

    selling_price DECIMAL(12,2)
        CHECK (selling_price >= cost_price)

);


-- Store Dimension

CREATE TABLE dim_store (

    store_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    store_name VARCHAR(100) NOT NULL,

    city VARCHAR(100),

    state VARCHAR(100),

    region VARCHAR(50),

    manager_name VARCHAR(100)

);


-- Promotion Dimension

CREATE TABLE dim_promotion (

    promotion_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    campaign_name VARCHAR(100),

    discount_percent DECIMAL(5,2)
        CHECK (discount_percent BETWEEN 0 AND 100),

    start_date DATE,

    end_date DATE,

    CHECK (end_date >= start_date)

);


-- Date Dimension

CREATE TABLE dim_date (

    date_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    full_date DATE UNIQUE,

    day INT,

    month INT,

    month_name VARCHAR(20),

    quarter INT,

    year INT,

    weekday VARCHAR(20),

    is_weekend BOOLEAN

);


-- Sales Fact Table


CREATE TABLE fact_sales (

    sales_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    customer_id INT NOT NULL,

    product_id INT NOT NULL,

    store_id INT NOT NULL,

    promotion_id INT,

    date_id INT NOT NULL,

    quantity INT
        CHECK (quantity > 0),

    unit_price DECIMAL(12,2)
        CHECK (unit_price >= 0),

    discount DECIMAL(12,2)
        CHECK (discount >= 0),

    sales_amount DECIMAL(12,2)
        CHECK (sales_amount >= 0),

    cost_price DECIMAL(12,2)
        CHECK (cost_price >= 0),

    profit DECIMAL(12,2),

    payment_method VARCHAR(20)
        CHECK (
            payment_method IN (
                'Cash',
                'Card',
                'UPI',
                'Net Banking'
            )
        ),

    order_status VARCHAR(20)
        CHECK (
            order_status IN (
                'Completed',
                'Returned',
                'Cancelled'
            )
        ),

    CONSTRAINT fk_customer
        FOREIGN KEY (customer_id)
        REFERENCES dim_customer(customer_id),

    CONSTRAINT fk_product
        FOREIGN KEY (product_id)
        REFERENCES dim_product(product_id),

    CONSTRAINT fk_store
        FOREIGN KEY (store_id)
        REFERENCES dim_store(store_id),

    CONSTRAINT fk_promotion
        FOREIGN KEY (promotion_id)
        REFERENCES dim_promotion(promotion_id),

    CONSTRAINT fk_date
        FOREIGN KEY (date_id)
        REFERENCES dim_date(date_id)

);