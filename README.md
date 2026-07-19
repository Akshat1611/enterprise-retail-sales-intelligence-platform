# 🛒 Retail Sales Analytics | End-to-End Data Engineering & Business Intelligence Project

An enterprise-grade Retail Sales Analytics project that demonstrates the complete data analytics lifecycle—from synthetic data generation and ETL to PostgreSQL data warehousing, SQL analytics, and interactive Power BI dashboards.

This project simulates a real retail business with realistic customers, products, stores, promotions, and millions of sales transactions, enabling advanced business analysis and visualization.

---

## 📌 Project Objectives

- Build a production-style retail data warehouse
- Generate realistic business data using Python
- Implement an ETL pipeline for loading data into PostgreSQL
- Perform advanced SQL analytics
- Develop executive-level Power BI dashboards
- Showcase skills relevant to Data Analyst, Business Analyst, and BI Developer roles

---

# 🏗️ Architecture

```
                  Python Data Generators
                          │
                          ▼
                Synthetic CSV Datasets
                          │
                          ▼
                  Python ETL Loaders
                          │
                          ▼
                PostgreSQL Data Warehouse
                          │
                          ▼
                 SQL Business Analytics
                          │
                          ▼
              Power BI Interactive Dashboard
```

---

# ⭐ Tech Stack

| Category | Technology |
|----------|------------|
| Programming | Python |
| Database | PostgreSQL |
| SQL | PostgreSQL SQL |
| Data Processing | Pandas |
| Data Generation | Faker |
| Database Connectivity | Psycopg2 |
| Environment | Python Virtual Environment |
| Version Control | Git & GitHub |
| BI Tool | Power BI |

---

# 📂 Project Structure

```
Retail-Sales-Analytics/
│
├── database/
│   └── schema.sql
│
├── python/
│   ├── config/
│   ├── database/
│   ├── generators/
│   ├── loaders/
│   └── utils/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── powerbi/
│
├── docs/
│
├── reports/
│
├── tests/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🗄️ Data Warehouse Design

The project follows a **Star Schema** architecture.

### Dimension Tables

- dim_customer
- dim_product
- dim_store
- dim_promotion
- dim_date

### Fact Table

- fact_sales

---

# 📊 Dataset

| Table | Records |
|--------|---------|
| Customers | 50,000 |
| Products | 5,000 |
| Stores | 500 |
| Promotions | 100 |
| Dates | 2,192 |
| Sales | 1,000,000+ (Planned) |

---

# ⚙️ ETL Pipeline

The project includes automated ETL scripts for:

- Customer Generation & Loading
- Product Generation & Loading
- Store Generation & Loading
- Promotion Generation & Loading
- Date Generation & Loading
- Sales Generation & Loading *(In Progress)*

---

# 📈 Business Analytics

The project will answer questions like:

- Total Revenue
- Monthly Sales Trend
- Regional Performance
- Product Performance
- Customer Segmentation
- Promotion Effectiveness
- Profitability Analysis
- Sales Forecasting
- RFM Analysis

---

# 📊 Power BI Dashboard

The dashboard will include:

- Executive Overview
- Revenue KPIs
- Monthly Sales Trends
- Category Analysis
- Regional Performance
- Customer Insights
- Promotion Performance
- Profit Analysis
- Interactive Filters & Drill-through

---

# 🚀 Getting Started

## Clone the Repository

```bash
git clone https://github.com/<your-username>/Retail-Sales-Analytics.git
```

## Navigate to the Project

```bash
cd Retail-Sales-Analytics
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Environment

### Windows

```bash
.\venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure Environment Variables

Create a `.env` file:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=RetailAnalytics
DB_USER=postgres
DB_PASSWORD=your_password
```

---

# 📋 Future Enhancements

- Sales Data Generator
- Incremental ETL
- Logging Framework
- Unit Testing
- Docker Support
- Airflow Pipeline
- Azure Deployment
- Power BI Service Publishing

---

# 📸 Screenshots

Coming Soon

- PostgreSQL Schema
- Power BI Dashboard
- SQL Query Results

---

# 📚 Skills Demonstrated

- Python
- SQL
- PostgreSQL
- ETL Pipeline Development
- Data Warehousing
- Star Schema Modeling
- Data Generation
- Pandas
- Git
- GitHub
- Power BI
- Business Intelligence
- Data Analytics

---

# 👨‍💻 Author

**Akshat Sharma**

MBA Business Analytics | Data Analyst | Python | SQL | PostgreSQL | Power BI

LinkedIn: *(Add your profile)*

GitHub: *(Add your GitHub profile)*

---

## ⭐ If you found this project helpful, consider giving it a star!