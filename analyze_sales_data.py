#!/usr/bin/env python3
"""
analyze_sales_data.py

Professional Sales Analysis Script
----------------------------------
This script performs a full sales analysis using the Superstore dataset.

Features:
- Flexible encoding handling
- Data cleaning and preparation
- Monthly revenue analysis
- Year-over-Year (YoY) analysis
- Regional performance evaluation
- Top customer revenue contribution
- Automated visualization export
- Text-based insights generation

Outputs:
    - sales_cleaned.csv
    - summary_metrics.csv
    - monthly_revenue_trend.png
    - yoy_multiline_trend.png
    - yoy_growth_chart.png
    - revenue_by_region.png
    - top_customers.png
    - insights_summary.txt
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --------------------------------------------------------------------
# CONFIGURATION
# --------------------------------------------------------------------

DATA_PATH = r"C:\Users\HP\Documents\Granger_Analytics\Portfolio\Python_Data_Cleaning\superstore_final_dataset.csv"
OUTPUT_DIR = r"C:\Users\HP\Documents\Granger_Analytics\Portfolio\Python_Data_Cleaning"

CLEANED_DATA = "sales_cleaned.csv"
SUMMARY_METRICS = "summary_metrics.csv"
INSIGHTS_TXT = "insights_summary.txt"

# Plots
MONTHLY_PLOT = "monthly_revenue_trend.png"
YOY_MULTI_PLOT = "yoy_multiline_trend.png"
YOY_GROWTH_PLOT = "yoy_growth_chart.png"
REGION_PLOT = "revenue_by_region.png"
TOP_CUSTOMERS_PLOT = "top_customers.png"

os.makedirs(OUTPUT_DIR, exist_ok=True)


# --------------------------------------------------------------------
# DATA LOADING
# --------------------------------------------------------------------

def load_data(path):
    encodings = ["utf-8", "latin1", "cp1252"]

    for enc in encodings:
        try:
            df = pd.read_csv(path, encoding=enc)
            df.columns = [col.strip() for col in df.columns]
            print(f"File loaded using encoding: {enc}")
            return df
        except UnicodeDecodeError:
            print(f"Encoding failed: {enc}. Trying next...")

    raise ValueError("Unable to read the CSV. Try re-saving as UTF-8.")


def inspect_data(df):
    print("\nPreview:")
    print(df.head())
    print("\nInfo:")
    print(df.info())


# --------------------------------------------------------------------
# DATA CLEANING
# --------------------------------------------------------------------

def clean_data(df):
    df = df.copy()

    df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
    df = df.dropna(subset=["Sales"])

    df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")

    df["Year"] = df["Order_Date"].dt.year
    df["Month"] = df["Order_Date"].dt.month
    df["Order_Month"] = df["Order_Date"].dt.to_period("M").astype(str)

    df = df.drop_duplicates()

    return df


# --------------------------------------------------------------------
# KPI CALCULATION
# --------------------------------------------------------------------

def compute_kpis(df):
    return {
        "Total_Sales": df["Sales"].sum(),
        "Total_Orders": len(df),
        "Unique_Customers": df["Customer_ID"].nunique(),
        "Average_Order_Value": df["Sales"].mean()
    }


# --------------------------------------------------------------------
# ANALYTICS FUNCTIONS
# --------------------------------------------------------------------

def monthly_trend(df):
    monthly = df.groupby("Order_Month")["Sales"].sum().reset_index()
    return monthly.sort_values("Order_Month")


def revenue_by_region(df):
    return (
        df.groupby("Region")["Sales"]
        .sum()
        .reset_index()
        .sort_values("Sales", ascending=False)
    )


def top_customers(df, n=10):
    return (
        df.groupby("Customer_Name")["Sales"]
        .sum()
        .reset_index()
        .sort_values("Sales", ascending=False)
        .head(n)
    )


# --------------------------------------------------------------------
# YEAR-OVER-YEAR ANALYSIS
# --------------------------------------------------------------------

def yearly_trend(df):
    """Returns revenue grouped by Year and Month."""
    grouped = (
        df.groupby(["Year", "Month"])["Sales"]
        .sum()
        .reset_index()
        .sort_values(["Year", "Month"])
    )
    return grouped


def yoy_pivot(df):
    """Returns pivot table: Month x Year, plus YoY percentage growth."""
    pivot = df.pivot_table(
        values="Sales",
        index="Month",
        columns="Year",
        aggfunc="sum"
    )

    # Calculate YoY Growth between last two years only (most recent comparison)
    years = sorted(list(pivot.columns))
    if len(years) >= 2:
        pivot["YoY_Growth_%"] = (
            (pivot[years[-1]] - pivot[years[-2]]) / pivot[years[-2]] * 100
        )
    else:
        pivot["YoY_Growth_%"] = None

    return pivot


# --------------------------------------------------------------------
# VISUALIZATIONS
# --------------------------------------------------------------------

def plot_monthly_revenue(monthly_df, path):
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=monthly_df, x="Order_Month", y="Sales", marker="o")
    plt.title("Monthly Revenue Trend")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(path, dpi=200)
    plt.close()


def plot_revenue_by_region(region_df, path):
    plt.figure(figsize=(8, 5))
    sns.barplot(data=region_df, x="Region", y="Sales")
    plt.title("Revenue by Region")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(path, dpi=200)
    plt.close()


def plot_top_customers(top_df, path):
    plt.figure(figsize=(10, 8))
    sns.barplot(data=top_df, y="Customer_Name", x="Sales")
    plt.title("Top Customers")
    plt.tight_layout()
    plt.savefig(path, dpi=200)
    plt.close()


def plot_yoy_multiline(df, path):
    """Multi-line plot showing Month vs Sales for each Year."""
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df, x="Month", y="Sales", hue="Year", marker="o")
    plt.title("Year-over-Year Revenue Trend")
    plt.xticks(range(1, 13))
    plt.tight_layout()
    plt.savefig(path, dpi=200)
    plt.close()


def plot_yoy_growth(pivot_df, path):
    """Bar chart of YoY % Growth for each Month."""
    if "YoY_Growth_%" not in pivot_df.columns:
        return

    plt.figure(figsize=(10, 6))
    sns.barplot(x=pivot_df.index, y=pivot_df["YoY_Growth_%"])
    plt.title("Year-over-Year Monthly Growth (%)")
    plt.xlabel("Month")
    plt.ylabel("Growth %")
    plt.tight_layout()
    plt.savefig(path, dpi=200)
    plt.close()


# --------------------------------------------------------------------
# INSIGHT GENERATION
# --------------------------------------------------------------------

def generate_insights(kpis, region_df, top_customers_df, yoy_df):
    insights = []
    insights.append("INSIGHTS SUMMARY")
    insights.append("--------------------------------------------------")
    insights.append(f"Total Revenue: ${kpis['Total_Sales']:,.2f}")
    insights.append(f"Total Orders: {kpis['Total_Orders']:,}")
    insights.append(f"Unique Customers: {kpis['Unique_Customers']:,}")
    insights.append(f"Average Order Value: ${kpis['Average_Order_Value']:,.2f}")

    # Regional Insight
    if len(region_df) > 0:
        r = region_df.iloc[0]
        insights.append(
            f"\nTop Region: {r['Region']} "
            f"(${r['Sales']:,.2f})"
        )

    # Top Customer
    if len(top_customers_df) > 0:
        c = top_customers_df.iloc[0]
        insights.append(
            f"Top Customer: {c['Customer_Name']} "
            f"(${c['Sales']:,.2f})"
        )

    # YoY Insights
    if "YoY_Growth_%" in yoy_df.columns:
        latest_growth = yoy_df["YoY_Growth_%"].mean()
        insights.append("\nYear-over-Year Overview:")
        insights.append(f"Average YoY Growth: {latest_growth:.2f}%")

        best_month = yoy_df["YoY_Growth_%"].idxmax()
        worst_month = yoy_df["YoY_Growth_%"].idxmin()

        insights.append(
            f"Strongest YoY Month: {best_month} "
            f"({yoy_df.loc[best_month,'YoY_Growth_%']:.2f}%)"
        )
        insights.append(
            f"Weakest YoY Month: {worst_month} "
            f"({yoy_df.loc[worst_month,'YoY_Growth_%']:.2f}%)"
        )

    # Recommendations
    insights.append("\nRecommended Actions:")
    insights.append("1. Strengthen marketing in high-performing regions.")
    insights.append("2. Expand loyalty programs for top customers.")
    insights.append("3. Investigate weak YoY months for operational improvement.")
    insights.append("4. Analyze product categories to refine performance strategy.")

    return "\n".join(insights)


# --------------------------------------------------------------------
# MAIN EXECUTION
# --------------------------------------------------------------------

def main():
    print("Loading data...")
    df = load_data(DATA_PATH)
    inspect_data(df)

    print("\nCleaning data...")
    df_clean = clean_data(df)
    df_clean.to_csv(os.path.join(OUTPUT_DIR, CLEANED_DATA), index=False)

    print("\nComputing KPIs...")
    kpis = compute_kpis(df_clean)

    print("\nRunning analysis...")
    monthly_df = monthly_trend(df_clean)
    region_df = revenue_by_region(df_clean)
    top_cust_df = top_customers(df_clean)

    # Yearly analysis
    yearly_df = yearly_trend(df_clean)
    yoy_df = yoy_pivot(yearly_df)

    pd.DataFrame([kpis]).to_csv(
        os.path.join(OUTPUT_DIR, SUMMARY_METRICS),
        index=False
    )

    print("\nGenerating visualizations...")
    plot_monthly_revenue(monthly_df, os.path.join(OUTPUT_DIR, MONTHLY_PLOT))
    plot_revenue_by_region(region_df, os.path.join(OUTPUT_DIR, REGION_PLOT))
    plot_top_customers(top_cust_df, os.path.join(OUTPUT_DIR, TOP_CUSTOMERS_PLOT))
    plot_yoy_multiline(yearly_df, os.path.join(OUTPUT_DIR, YOY_MULTI_PLOT))
    plot_yoy_growth(yoy_df, os.path.join(OUTPUT_DIR, YOY_GROWTH_PLOT))

    print("\nWriting insights...")
    insights = generate_insights(kpis, region_df, top_cust_df, yoy_df)
    with open(os.path.join(OUTPUT_DIR, INSIGHTS_TXT), "w") as f:
        f.write(insights)

    print("\nAnalysis complete.")
    print("Files saved in:", OUTPUT_DIR)
    print("\n--- INSIGHTS ---")
    print(insights)


if __name__ == "__main__":
    main()
