# BikeHubProject
# 🚲 End-to-End Data Lakehouse

## 🎯 Project Goal
To transform raw sales and customer CRM data into a high-performance **Star Schema (Gold Layer)** for executive BI reporting using Databricks and Delta Lake.

---

## 🏗️ Architecture Overview

This project follows the **Medallion Architecture** to ensure data quality and traceability:

### 🥈 Silver Layer
Cleansed relational data including:
- `crm_sales`
- `dim_customer`
- `dim_products`

### 🥇 Gold Layer
Business-ready **Star Schema**.

#### Fact Table
- `fact_sales`

#### Dimension Tables
- `dim_date`
- `dim_customer`
- `dim_products`

---

## 🛠️ Technical Implementation

### 1️⃣ Data Modeling & Surrogate Keys

- Implemented a **Star Schema** to optimize query performance.
- Generated **Identity Columns (BIGINT)** for surrogate keys in dimension tables.
- Mapped Sales natural keys to surrogate keys using high-performance joins.
- Created a comprehensive `dim_date` table to support **Time-Series Analysis**.

---

### 2️⃣ Advanced Data Cleaning (ETL)

#### 🔑 Key Resolving
- Applied `SUBSTRING` logic to resolve prefix mismatches between sales systems and product catalogs.

#### 🧩 Data Imputation
- Used SQL Window Functions:
  - `MAX() OVER (PARTITION BY ...)`
- Filled missing `order_date` values at the line-item level using order header data.

#### ✅ Constraint Enforcement
- Enforced `NOT NULL` constraints on core measures:
  - `Price`
  - `Revenue`
- Ensured the Gold Layer remains a **Single Source of Truth**.

---

## 📊 Business Insights Derived

After engineering the Gold Layer, the schema was used to answer key business questions:

### 🌍 Global Market Ranking
- Identified top-performing countries by:
  - Total revenue
  - Unique customer reach

### 👥 Customer Segmentation
- Categorized **"Lifetime VIPs"** using:
  - Age-group bucketing (`CASE` logic)
- Ranked customers by country-specific spending.

### 🚴 Product Performance
- Analyzed **Revenue vs. Units Sold** across four product families:
  - Road
  - Mountain
  - Sport
  - Touring
---

## 📈 Tools Used

### Language
- PySpark
- Spark SQL
### Storage
- Delta Lake
### Platform
- Databricks