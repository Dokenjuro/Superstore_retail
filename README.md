# Superstore Sales Analysis — Portfolio Case Study

**Author:** Chiedozie Charles Chigboh  
**Role:** Data Analyst  
**Project Type:** Exploratory Sales Analysis  
**Dataset:** Superstore Retail Sales Data (2015–2018)

---

## 1. Project Overview

This project presents a full analytical workflow applied to a four-year retail sales dataset. It includes data preparation, key performance metrics, regional and customer segmentation, temporal trend analysis, and year-over-year (YoY) performance evaluation.

The entire workflow is automated using a single Python script, enabling reproducible analysis suitable for executive-level reporting and strategic planning.

### **Deliverables include:**

- Cleaned dataset  
- KPI summary file  
- Monthly revenue trend visualization  
- Year-over-year trend visualization (multi-line)  
- YoY monthly growth visualization  
- Regional revenue performance chart  
- Top customer analysis  
- Text-based insights report  

This project demonstrates advanced analytical structuring suitable for stakeholder reporting and executive dashboards.

---

## 2. Objectives

The analysis aims to answer the following business questions:

1. What are the key sales performance indicators?  
2. How does revenue trend month-to-month over time?  
3. How does revenue compare across different regions?  
4. Which customers contribute most significantly to sales?  
5. How do revenues change year-over-year?  
6. What strategic insights can be drawn from these trends?

---

## 3. Dataset Description

The Superstore dataset contains detailed order-level records, including:

- **Order information:** Order ID, Order Date, Ship Date  
- **Customer data:** Customer ID, Customer Name, Segment  
- **Geographical attributes:** City, State, Region  
- **Product attributes:** Category, Sub-Category, Product Name  
- **Metrics:** Sales  

The dataset covers **2015 through 2018**, enabling multi-year comparison and trend analysis.

---

## 4. Methodology

This project follows a structured and reproducible analytical workflow.

---

### **4.1 Data Loading**

- Multiple encodings evaluated for compatibility  
- Automatic fallback logic to avoid Unicode errors  
- Column names standardized for consistency  

---

### **4.2 Data Cleaning**

- Conversion of Sales to numeric  
- Full date parsing  
- Extraction of Year, Month, and Year-Month (Order_Month) fields  
- Removal of duplicate records  
- Verification of required fields  

---

### **4.3 Feature Engineering**

- Monthly revenue aggregation  
- Regional revenue grouping  
- Customer-level revenue ranking  
- Creation of Year-Month period identifiers  
- Pivot-table structures for YoY analysis  

---

### **4.4 Analysis**

- Total sales, unique customers, order volume  
- Month-by-month revenue timeline  
- Year-over-year comparison across all months  
- Region-level performance  
- Top customer identification  

---

### **4.5 Visualization**

All charts exported as PNG files, including:

- **Monthly Revenue Trend**  
- **Year-over-Year Multi-Line Trend**  
- **YoY Monthly Growth Percentage**  
- **Regional Revenue Bar Chart**  
- **Top Customer Revenue Chart**

---

### **4.6 Insight Development**

The automated insight generator produces a structured narrative summarizing:

- Core KPIs  
- Highest-performing regions  
- Top customers  
- Seasonality patterns  
- Year-over-year performance  
- Actionable recommendations  

---

## 5. Key Insights

### **5.1 Sales Performance**

Sales activity remains consistent across the four-year period, exhibiting seasonal changes and varying month-to-month demand levels.

---

### **5.2 Regional Contribution**

One region consistently contributes a disproportionately high share of total revenue. This offers a model for scaling regional success patterns to lower-performing markets.

---

### **5.3 Customer Concentration**

A relatively small proportion of customers accounts for a significant percentage of total revenue. These individuals represent strong candidates for targeted loyalty, retention, and value expansion programs.

---

### **5.4 Year-over-Year Trends**

- Monthly YoY comparisons reveal fluctuating performance.  
- Specific months outperform their prior-year equivalents, while others underperform.  
- These insights can guide pricing strategies, marketing timing, and inventory planning.

---

## 6. Visualizations

| Visualization | File |
|---------------|-------|
| Monthly Revenue Trend | `monthly_revenue_trend.png` |
| Year-over-Year Multi-Line Trend | `yoy_multiline_trend.png` |
| YoY Monthly Growth (%) | `yoy_growth_chart.png` |
| Revenue by Region | `revenue_by_region.png` |
| Top Customers by Revenue | `top_customers.png` |

---



## 🧰 File Structure

      ```bash
         
         Granger_Analytics/
         └── Portfolio/
            └── Superstore_Analysis/
               ├── analyze_sales_data.py
               ├── sales_cleaned.csv
               ├── summary_metrics.csv
               ├── Superstore_final_dataset.csv
               ├── monthly_revenue_trend.png
               ├── yoy_multiline_trend.png
               ├── yoy_growth_chart.png
               ├── revenue_by_region.png
               ├── top_customers.png
               ├── insights_summary.txt
               ├── Superstore Sales Analysis — Case Study Report.md
               └── README.md


---


## 7. Tools & Technologies

| Purpose             | Tools                         |
| ------------------- | ----------------------------- |
| **Programming**     | Python 3.11                   |
| **Libraries**       | Pandas, Matplotlib, Seaborn   |
| **Editor**          | VS Code (Virtual Environment) |
| **Version Control** | Git & GitHub                  |
| **Data Format**     | CSV                           |

---

## 8. How to reproduce

1. Clone this repository:

```bash
   git clone https://github.com/dokenjuro/Granger_Analytics.git
   cd Granger_Analytics/Portfolio/Superstore_Analysis
```
2. Activate your virtual environment:

```bash
   env\Scripts\activate
   ```
3. Run the Script:
```bash
   python analyze_sales_data.py
   ```
4. Check the output visualizations in the same directory.



## 9. Conclusion

This project delivers a complete sales analytics workflow, including KPI evaluation, regional and customer segmentation, time-series analysis, and year-over-year comparison.
The script is built for automation, clarity, and practical interpretability, making it suitable for operational analytics or portfolio demonstration

© 2025 — Chiedozie Chigboh | Business Analytics & AI Portfolio
