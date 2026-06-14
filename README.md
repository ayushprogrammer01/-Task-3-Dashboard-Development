# 📊 Task 3 – Dashboard Development

**Internship:** CODTECH IT Solutions – Data Analytics  
**Task:** Interactive Dashboard Development using Dash & Plotly  
**Tool Used:** Python · Dash · Plotly · Pandas

---

## 📋 Internship Details

| Field | Details |
|-------|---------|
| **Name** | Ayush Kumar Singh |
| **Company** | CODTECH IT Solutions Pvt. Ltd. |
| **Intern ID** | CITS527 |
| **Domain** | Data Analytics |
| **Duration** | 4 Weeks |
| **Mentor** | Neela Santhosh Kumar |

---

## 📌 Objective

Build a fully functional, interactive analytics dashboard that visualizes a retail sales dataset and delivers actionable business insights through dynamic charts, KPI cards, and filter controls.

---

## 📁 Project Structure

```
Task-3-Dashboard-Development/
│
├── app.py              # Main Dash application (dashboard code)
├── sales_data.csv      # Dataset – 100 sales records across 2024
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## 📊 Dataset Overview

**File:** `sales_data.csv`  
**Records:** 100 transactions  
**Period:** January 2024 – December 2024

| Column | Description |
|---|---|
| Order_ID | Unique order identifier |
| Date | Transaction date |
| Category | Product category (Technology, Furniture, Office Supplies) |
| Sub_Category | Product sub-category |
| Product | Product name |
| Region | Sales region (East, West, Central, South) |
| Sales | Revenue from the order (₹) |
| Quantity | Number of units sold |
| Discount | Discount applied (0.0 to 0.2) |
| Profit | Profit earned (₹) |

---

## 📈 Dashboard Features

### 🔵 KPI Summary Cards
- **Total Sales** – Sum of all revenue
- **Total Profit** – Sum of all profits
- **Total Orders** – Count of transactions
- **Average Discount** – Mean discount rate
- **Profit Margin** – Profit as % of sales

### 📉 Interactive Charts
1. **Monthly Sales & Profit Trend** – Line chart tracking revenue and profit month-wise
2. **Sales by Category** – Donut chart showing share of each product category
3. **Sales by Region** – Horizontal bar chart comparing regional performance
4. **Profit vs Sales (Scatter)** – Bubble chart by sub-category to spot profitable segments
5. **Top 10 Products by Sales** – Horizontal bar chart of best-selling products
6. **Discount vs Profit (Regression)** – Scatter plot with trend line showing discount impact

### 🎛️ Filters (all charts update live)
- **Category** – Filter by Technology / Furniture / Office Supplies
- **Region** – Filter by East / West / Central / South
- **Date Range** – Select any custom date window

---

## 🚀 How to Run

### Step 1 – Clone / Download
```bash
git clone https://github.com/your-username/your-repo.git
cd Task-3-Dashboard-Development
```

### Step 2 – Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3 – Run the Dashboard
```bash
python app.py
```

### Step 4 – Open in Browser
Navigate to: **http://127.0.0.1:8050/**

---

## 💡 Actionable Insights from the Dashboard

1. **Technology dominates revenue** – phones and laptops generate the highest sales and profit margins.
2. **Higher discounts reduce profit** – the scatter plot shows a negative correlation between discount rate and profit.
3. **Q4 peaks** – November and December record the highest monthly sales due to holiday demand.
4. **South region underperforms** – consistent lower sales compared to East and West regions.
5. **Office Supplies have thin margins** – high volume but low profit per unit.

---

## 🛠️ Technologies Used

| Tool | Purpose |
|---|---|
| Python 3.14.5 | Core programming language |
| Dash 2.x | Web framework for the dashboard |
| Plotly | Interactive charting library |
| Pandas | Data loading and manipulation |
| Statsmodels | OLS trend line in scatter plot |

