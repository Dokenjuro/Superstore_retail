# Superstore Sales Analysis — Case Study Report

**Author:** Chiedozie Charles Chigboh  
**Role:** Data Analyst  
**Project Type:** Exploratory Sales & Performance Analysis  
**Dataset:** Superstore Retail Sales Data (2015–2018)  
**Tools Used:** Python (Pandas, Matplotlib, Seaborn), Git, VS Code  

---

## 1. Business Context
A retail company with stores across different regions in the United States wanted a clearer picture of how its sales behaved over four years. Leadership wanted insight into:

- Overall revenue trends over time  
- Regions contributing the strongest numbers  
- High-value customers  
- Monthly revenue rhythms  
- Business actions that could improve performance  

This work provides structured guidance for revenue growth, smarter marketing choices, and stronger customer relationships.

---

## 2. Business Questions
The project focused on these key questions:

1. What does overall sales performance look like across the dataset?  
2. How does revenue shift month-to-month?  
3. Which regions bring in the highest revenue and potential growth?  
4. Who are the top-value customers?  
5. How does performance change year-over-year?  
6. What practical recommendations can be drawn from the results?

---

## 3. Dataset Summary
The dataset covers 2015–2018 and includes:

- **Order details:** IDs, order dates, ship dates, priority levels  
- **Customer information:** IDs, names, segments  
- **Geography:** city, state, postal code, region  
- **Product attributes:** category, sub-category, name, SKU  
- **Numeric fields:** sales, quantity, discount, profit  

This timeframe allows detection of seasonal patterns and multi-year trends.

---

## 4. Analytical Approach

### 4.1 Data Loading
Tested multiple text encodings to read files correctly; fallback logic handled unusual characters in CSVs.

### 4.2 Data Cleaning and Validation
- Converted sales to numeric values  
- Parsed order dates  
- Created year and month fields  
- Removed duplicates and handled missing values  
- Standardized column names  

### 4.3 Feature Engineering
- Added fields for month tracking and summarizing trends  
- Grouped data by region and customer for segmentation  

### 4.4 Computation of Key Metrics
- Total revenue, total orders, unique customers, average order value  
- Breakdowns by region, customer, and month  

### 4.5 Exploratory Data Analysis (EDA)
- Monthly revenue trends  
- Regional revenue contributions  
- High-value customer distribution  
- Year-over-year patterns  
- Seasonal fluctuations  

### 4.6 Visualization
- Monthly revenue trends  
- Regional revenue contributions  
- Top customers  
- YoY multi-line views  
- Monthly YoY growth charts  

All charts were saved as PNG files.

---

## 5. Findings and Insights

### 5.1 Overall Sales Performance
Sales were fairly consistent over four years, supported by steady customer activity and moderate order sizes.

### 5.2 Monthly Performance
Monthly trends revealed predictable seasonal cycles; certain months showed higher activity indicating promotions or industry patterns.

### 5.3 Regional Revenue Assessment
One region consistently led in revenue with a strong mix of frequent orders and valuable customers. Other regions could benefit from focused marketing.

### 5.4 Customer Concentration
A small group of customers contributed disproportionately to revenue, highlighting retention and loyalty opportunities.

### 5.5 Year-over-Year Performance
YoY analysis showed some months improving while others dipped. Trends point to operational, seasonal, or competitive influences.

---

## 6. Recommendations
1. **Strengthen marketing** in high-performing regions  
2. **Establish loyalty programs** for high-value customers  
3. **Investigate underperforming months** for stock, pricing, or promotion adjustments  
4. **Conduct category-level analysis** for slower-performing products  
5. **Leverage seasonal peaks** for targeted promotions  

---

## 7. Technical Assets
- Cleaned dataset (`sales_cleaned.csv`)  
- Summary metrics (`summary_metrics.csv`)  
- Trend visuals (`*.png`)  
- Insights summary (`insights_summary.txt`)  
- Python script (`analyze_sales_data.py`) for automation  

---

## 8. Tools and Technologies Used
- Python (Pandas, Matplotlib, Seaborn)  
- VS Code  
- Git & GitHub  
- CSV as data source  

---

## 9. Conclusion
The analysis provides a clear view of sales patterns across four years, with actionable insights on regional strengths, customer value distribution, seasonal behavior, and year-over-year trends. The visuals, metrics, and scripts offer a solid foundation for reporting or integration into a full BI dashboard.

---

## Dataset Source
This project uses the **Superstore Sales Dataset** publicly available on Kaggle:  
Created by **Bhanu Pratap Biswas**  
https://www.kaggle.com/datasets/bhanupratapbiswas/superstore-sales

