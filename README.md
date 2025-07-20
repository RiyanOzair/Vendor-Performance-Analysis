# Vendor Performance Analysis Project

## 📊 Project Overview

This project provides a comprehensive analysis of vendor performance using supply chain data including purchases, sales, inventory, and pricing information. The analysis identifies key insights about vendor efficiency, profitability, inventory management, and strategic opportunities for business optimization.

## 🎯 Key Business Questions Answered

- **Vendor Performance**: Which vendors demonstrate the highest sales performance?
- **Profitability Analysis**: How do profit margins vary between high and low-performing vendors?
- **Inventory Management**: Which vendors have slow inventory turnover and excess stock?
- **Pricing Strategy**: Does bulk purchasing reduce unit prices, and what's the optimal volume?
- **Capital Efficiency**: How much capital is locked in unsold inventory per vendor?
- **Market Opportunities**: Which brands need promotional or pricing adjustments?

## 📁 Project Structure

```
Vendor Performance Project/
├── 📊 Data Analysis & Notebooks
│   ├── Vendor Performance Analysis.ipynb    # Main analysis notebook
│   ├── EDA-Vendor Performance Analysis.ipynb # Exploratory data analysis
│   └── final_summary_table.csv             # Processed dataset for analysis
│
├── 🗄️ Database & Data Processing
│   ├── inventory1.db                       # SQLite database with all tables
│   ├── Ingestion1_db.py                   # Data ingestion script
│   └── get_vendor_summary.py              # Creates final summary table
│
├── 📂 Raw Data Sources
│   └── Vendor Dataset/
│       ├── begin_inventory.csv            # Starting inventory levels
│       ├── end_inventory.csv              # Ending inventory levels
│       ├── purchases.csv                  # Purchase transactions
│       ├── purchase_prices.csv            # Purchase pricing data
│       ├── sales.csv                      # Sales transactions
│       └── vendor_invoice.csv             # Vendor invoice details
│
├── 📈 Dashboards & Visualizations
│   ├── Vendor Performance Analysis dashboard.pbix  # Power BI dashboard
│   └── Vendor Performance Dashboard Snapshot.gif   # Dashboard preview
│
├── 📝 Logs
│   └── Logs/
│       └── ingestion1_db.log              # Data processing logs
│
└── README.md                              # This file
```

## 🚀 Getting Started

### Prerequisites
```python
# Required Python packages
pandas
numpy
seaborn
matplotlib
sqlite3
scipy
plotly
warnings
```

### Quick Start Guide

1. **Data Ingestion** (if starting from raw data):
   ```python
   python Ingestion1_db.py
   ```

2. **Generate Summary Table**:
   ```python
   python get_vendor_summary.py
   ```

3. **Run Analysis**:
   Open `Vendor Performance Analysis.ipynb` and run all cells

## 📊 Key Findings & Insights

### 🏆 Top Performing Vendors
- **Highest Sales**: Vendors driving maximum revenue
- **Bulk Purchase Benefits**: Large orders achieve ~72% reduction in unit costs
- **Volume vs. Margin Trade-off**: High-performing vendors operate on lower margins (16-17%) but higher volumes

### 💰 Profitability Insights
- **Low-performing vendors** surprisingly have higher profit margins (43-46%)
- **High-performing vendors** sacrifice margin for volume (competitive pricing strategy)
- Strong correlation between purchase quantity and sales quantity (1.00)

### 📦 Inventory Management
- **Capital Locked**: Significant unsold inventory value identified per vendor
- **Slow Movers**: Vendors with stock turnover < 1 indicate excess inventory
- **Stock Turnover** negatively correlates with profit margins (-0.40)

### 🎯 Strategic Opportunities
- **Promotional Candidates**: Brands with low sales but high margins identified for marketing focus
- **Pricing Optimization**: Bulk purchasing strategies show clear cost benefits
- **Inventory Optimization**: Vendors with excess stock requiring attention

## 📈 Dashboard Features

The Power BI dashboard (`Vendor Performance Analysis dashboard.pbix`) includes:
- Vendor performance rankings
- Profit margin analysis
- Inventory turnover metrics
- Sales trend analysis
- Interactive filters by vendor, product, and time period

## 🔬 Statistical Analysis

### Hypothesis Testing Results
- **Research Question**: Is there a significant difference in profit margins between top and low-performing vendors?
- **Method**: Two-sample t-test
- **Result**: Statistically significant difference confirmed (p < 0.05)
- **Conclusion**: Low-performing vendors do have significantly higher profit margins

## 📊 Data Model

The analysis combines multiple data sources:
- **Purchases**: Transaction-level purchase data
- **Sales**: Sales transactions and quantities
- **Inventory**: Beginning and ending stock levels
- **Pricing**: Purchase prices and actual selling prices
- **Vendors**: Vendor information and invoicing

## 🔧 Technical Implementation

### Database Schema
- SQLite database with normalized tables
- Complex SQL queries for data aggregation
- Calculated metrics for performance analysis

### Analysis Approach
1. **Data Cleaning**: Remove negative profits and inconsistencies
2. **Feature Engineering**: Create calculated metrics (profit margins, turnover rates)
3. **Statistical Analysis**: Correlation analysis and hypothesis testing
4. **Visualization**: Interactive plots and business intelligence dashboards

## 📝 Future Enhancements

- **Predictive Analytics**: Forecast vendor performance trends
- **Automated Reporting**: Scheduled dashboard updates
- **Cost Analysis**: Deeper dive into freight and operational costs
- **Seasonality Analysis**: Identify seasonal patterns in vendor performance

## 🤝 Contributing

This project serves as a comprehensive template for vendor performance analysis. Feel free to adapt the methodology for your specific business needs.

## 📧 Contact

For questions about this analysis or methodology, please refer to the detailed documentation within the Jupyter notebooks.

---

*Last Updated: July 2025*
