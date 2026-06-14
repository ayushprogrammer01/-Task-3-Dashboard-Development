"""
CODTECH IT SOLUTIONS - Data Analytics Internship
Task 3: Dashboard Development
Author: Ayush Kumar Singh
Description: Interactive Sales Analytics Dashboard built with Dash & Plotly
"""

import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# ── Load & Prepare Data ──────────────────────────────────────────────────────
df = pd.read_csv("sales_data.csv", parse_dates=["Date"])
df["Month"] = df["Date"].dt.to_period("M").astype(str)
df["Month_Name"] = df["Date"].dt.strftime("%b %Y")

# ── App Init ─────────────────────────────────────────────────────────────────
app = dash.Dash(__name__, title="Sales Analytics Dashboard")

# ── Color Palette ────────────────────────────────────────────────────────────
COLORS = {
    "bg": "#F0F2F5",
    "card": "#FFFFFF",
    "primary": "#2563EB",
    "accent": "#16A34A",
    "danger": "#DC2626",
    "text": "#1E293B",
    "muted": "#64748B",
}

CATEGORY_COLORS = {
    "Technology": "#2563EB",
    "Furniture": "#7C3AED",
    "Office Supplies": "#EA580C",
}

# ── Reusable Card ────────────────────────────────────────────────────────────
def kpi_card(title, value, subtitle="", color=COLORS["primary"]):
    return html.Div([
        html.P(title, style={"margin": "0 0 4px", "fontSize": "13px",
                              "color": COLORS["muted"], "fontWeight": "600",
                              "textTransform": "uppercase", "letterSpacing": "0.05em"}),
        html.H2(value, style={"margin": "0", "fontSize": "28px",
                               "fontWeight": "800", "color": color}),
        html.P(subtitle, style={"margin": "4px 0 0", "fontSize": "12px",
                                 "color": COLORS["muted"]}),
    ], style={
        "background": COLORS["card"],
        "borderRadius": "12px",
        "padding": "20px 24px",
        "boxShadow": "0 1px 4px rgba(0,0,0,0.08)",
        "borderLeft": f"4px solid {color}",
        "flex": "1",
        "minWidth": "160px",
    })

# ── Layout ───────────────────────────────────────────────────────────────────
app.layout = html.Div(style={"background": COLORS["bg"], "minHeight": "100vh",
                               "fontFamily": "'Segoe UI', sans-serif", "padding": "0"}, children=[

    # Header
    html.Div([
        html.Div([
            html.H1("📊 Sales Analytics Dashboard",
                    style={"margin": "0", "fontSize": "24px", "fontWeight": "800",
                           "color": "#FFFFFF"}),
            html.P("CODTECH IT Solutions · Data Analytics Internship · Task 3",
                   style={"margin": "4px 0 0", "fontSize": "13px", "color": "#BFDBFE"}),
        ]),
        html.Div("2024 Annual Report", style={
            "background": "rgba(255,255,255,0.15)", "borderRadius": "8px",
            "padding": "8px 16px", "color": "white", "fontSize": "13px", "fontWeight": "600"
        })
    ], style={
        "background": "linear-gradient(135deg, #1E40AF 0%, #2563EB 100%)",
        "padding": "20px 32px", "display": "flex",
        "justifyContent": "space-between", "alignItems": "center",
        "boxShadow": "0 2px 8px rgba(0,0,0,0.15)"
    }),

    # Filters
    html.Div([
        html.Div([
            html.Label("Category", style={"fontWeight": "600", "fontSize": "13px",
                                           "color": COLORS["muted"], "marginBottom": "6px", "display": "block"}),
            dcc.Dropdown(
                id="category-filter",
                options=[{"label": c, "value": c} for c in sorted(df["Category"].unique())],
                placeholder="All Categories",
                multi=True,
                style={"fontSize": "14px"}
            )
        ], style={"flex": "1", "minWidth": "200px"}),

        html.Div([
            html.Label("Region", style={"fontWeight": "600", "fontSize": "13px",
                                         "color": COLORS["muted"], "marginBottom": "6px", "display": "block"}),
            dcc.Dropdown(
                id="region-filter",
                options=[{"label": r, "value": r} for r in sorted(df["Region"].unique())],
                placeholder="All Regions",
                multi=True,
                style={"fontSize": "14px"}
            )
        ], style={"flex": "1", "minWidth": "200px"}),

        html.Div([
            html.Label("Date Range", style={"fontWeight": "600", "fontSize": "13px",
                                             "color": COLORS["muted"], "marginBottom": "6px", "display": "block"}),
            dcc.DatePickerRange(
                id="date-filter",
                start_date=df["Date"].min(),
                end_date=df["Date"].max(),
                display_format="MMM DD, YYYY",
                style={"fontSize": "14px"}
            )
        ], style={"flex": "2", "minWidth": "280px"}),
    ], style={
        "background": COLORS["card"], "padding": "20px 32px",
        "display": "flex", "gap": "24px", "flexWrap": "wrap",
        "alignItems": "flex-end", "boxShadow": "0 1px 3px rgba(0,0,0,0.06)"
    }),

    # Main Content
    html.Div(style={"padding": "24px 32px"}, children=[

        # KPI Row
        html.Div(id="kpi-row", style={"display": "flex", "gap": "16px",
                                       "flexWrap": "wrap", "marginBottom": "24px"}),

        # Charts Row 1
        html.Div([
            html.Div([
                html.H3("Monthly Sales & Profit Trend", style={
                    "margin": "0 0 16px", "fontSize": "16px",
                    "fontWeight": "700", "color": COLORS["text"]}),
                dcc.Graph(id="line-chart", config={"displayModeBar": False})
            ], style={"background": COLORS["card"], "borderRadius": "12px",
                      "padding": "20px", "flex": "2", "minWidth": "300px",
                      "boxShadow": "0 1px 4px rgba(0,0,0,0.08)"}),

            html.Div([
                html.H3("Sales by Category", style={
                    "margin": "0 0 16px", "fontSize": "16px",
                    "fontWeight": "700", "color": COLORS["text"]}),
                dcc.Graph(id="pie-chart", config={"displayModeBar": False})
            ], style={"background": COLORS["card"], "borderRadius": "12px",
                      "padding": "20px", "flex": "1", "minWidth": "260px",
                      "boxShadow": "0 1px 4px rgba(0,0,0,0.08)"}),
        ], style={"display": "flex", "gap": "16px", "flexWrap": "wrap", "marginBottom": "16px"}),

        # Charts Row 2
        html.Div([
            html.Div([
                html.H3("Sales by Region", style={
                    "margin": "0 0 16px", "fontSize": "16px",
                    "fontWeight": "700", "color": COLORS["text"]}),
                dcc.Graph(id="bar-region", config={"displayModeBar": False})
            ], style={"background": COLORS["card"], "borderRadius": "12px",
                      "padding": "20px", "flex": "1", "minWidth": "260px",
                      "boxShadow": "0 1px 4px rgba(0,0,0,0.08)"}),

            html.Div([
                html.H3("Profit vs Sales (by Sub-Category)", style={
                    "margin": "0 0 16px", "fontSize": "16px",
                    "fontWeight": "700", "color": COLORS["text"]}),
                dcc.Graph(id="scatter-chart", config={"displayModeBar": False})
            ], style={"background": COLORS["card"], "borderRadius": "12px",
                      "padding": "20px", "flex": "2", "minWidth": "300px",
                      "boxShadow": "0 1px 4px rgba(0,0,0,0.08)"}),
        ], style={"display": "flex", "gap": "16px", "flexWrap": "wrap", "marginBottom": "16px"}),

        # Charts Row 3
        html.Div([
            html.Div([
                html.H3("Top 10 Products by Sales", style={
                    "margin": "0 0 16px", "fontSize": "16px",
                    "fontWeight": "700", "color": COLORS["text"]}),
                dcc.Graph(id="top-products", config={"displayModeBar": False})
            ], style={"background": COLORS["card"], "borderRadius": "12px",
                      "padding": "20px", "flex": "1", "minWidth": "300px",
                      "boxShadow": "0 1px 4px rgba(0,0,0,0.08)"}),

            html.Div([
                html.H3("Discount vs Profit Margin", style={
                    "margin": "0 0 16px", "fontSize": "16px",
                    "fontWeight": "700", "color": COLORS["text"]}),
                dcc.Graph(id="discount-profit", config={"displayModeBar": False})
            ], style={"background": COLORS["card"], "borderRadius": "12px",
                      "padding": "20px", "flex": "1", "minWidth": "300px",
                      "boxShadow": "0 1px 4px rgba(0,0,0,0.08)"}),
        ], style={"display": "flex", "gap": "16px", "flexWrap": "wrap"}),

    ]),

    # Footer
    html.Div("CODTECH IT Solutions · Data Analytics Internship · Task 3 · Dashboard Development",
             style={"textAlign": "center", "padding": "16px", "fontSize": "12px",
                    "color": COLORS["muted"], "borderTop": "1px solid #E2E8F0",
                    "background": COLORS["card"]})
])


# ── Callbacks ─────────────────────────────────────────────────────────────────
def filter_df(categories, regions, start_date, end_date):
    filtered = df.copy()
    if categories:
        filtered = filtered[filtered["Category"].isin(categories)]
    if regions:
        filtered = filtered[filtered["Region"].isin(regions)]
    if start_date:
        filtered = filtered[filtered["Date"] >= start_date]
    if end_date:
        filtered = filtered[filtered["Date"] <= end_date]
    return filtered


@app.callback(
    Output("kpi-row", "children"),
    Output("line-chart", "figure"),
    Output("pie-chart", "figure"),
    Output("bar-region", "figure"),
    Output("scatter-chart", "figure"),
    Output("top-products", "figure"),
    Output("discount-profit", "figure"),
    Input("category-filter", "value"),
    Input("region-filter", "value"),
    Input("date-filter", "start_date"),
    Input("date-filter", "end_date"),
)
def update_dashboard(categories, regions, start_date, end_date):
    d = filter_df(categories, regions, start_date, end_date)

    # ── KPIs ──
    total_sales = d["Sales"].sum()
    total_profit = d["Profit"].sum()
    total_orders = len(d)
    avg_discount = d["Discount"].mean() * 100
    profit_margin = (total_profit / total_sales * 100) if total_sales > 0 else 0

    kpis = [
        kpi_card("Total Sales", f"₹{total_sales:,.0f}", f"{total_orders} orders", COLORS["primary"]),
        kpi_card("Total Profit", f"₹{total_profit:,.0f}", f"{profit_margin:.1f}% margin", COLORS["accent"]),
        kpi_card("Total Orders", f"{total_orders:,}", "transactions", "#7C3AED"),
        kpi_card("Avg. Discount", f"{avg_discount:.1f}%", "across all orders", COLORS["danger"]),
        kpi_card("Profit Margin", f"{profit_margin:.1f}%", "net profitability", "#0891B2"),
    ]

    chart_layout = dict(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Segoe UI", color=COLORS["text"]),
        margin=dict(l=10, r=10, t=10, b=10),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    )

    # ── Line Chart ──
    monthly = d.groupby("Month").agg(Sales=("Sales", "sum"), Profit=("Profit", "sum")).reset_index()
    fig_line = go.Figure()
    fig_line.add_trace(go.Scatter(x=monthly["Month"], y=monthly["Sales"],
                                   name="Sales", mode="lines+markers",
                                   line=dict(color=COLORS["primary"], width=2.5),
                                   marker=dict(size=6)))
    fig_line.add_trace(go.Scatter(x=monthly["Month"], y=monthly["Profit"],
                                   name="Profit", mode="lines+markers",
                                   line=dict(color=COLORS["accent"], width=2.5, dash="dot"),
                                   marker=dict(size=6)))
    fig_line.update_layout(**chart_layout, height=280,
                            xaxis=dict(showgrid=False, tickangle=-30),
                            yaxis=dict(showgrid=True, gridcolor="#F1F5F9"))

    # ── Pie Chart ──
    cat_sales = d.groupby("Category")["Sales"].sum().reset_index()
    fig_pie = px.pie(cat_sales, names="Category", values="Sales",
                     color="Category", color_discrete_map=CATEGORY_COLORS,
                     hole=0.45)
    fig_pie.update_traces(textposition="inside", textinfo="percent+label",
                          marker=dict(line=dict(color="white", width=2)))
    fig_pie.update_layout(**chart_layout, height=280, showlegend=False)

    # ── Bar Region ──
    reg_sales = d.groupby("Region")["Sales"].sum().reset_index().sort_values("Sales", ascending=True)
    fig_bar = px.bar(reg_sales, x="Sales", y="Region", orientation="h",
                     color="Sales", color_continuous_scale=["#BFDBFE", "#1D4ED8"])
    fig_bar.update_layout(**chart_layout, height=280, coloraxis_showscale=False,
                           xaxis=dict(showgrid=True, gridcolor="#F1F5F9"),
                           yaxis=dict(showgrid=False))

    # ── Scatter Chart ──
    sub_agg = d.groupby(["Sub_Category", "Category"]).agg(
        Sales=("Sales", "sum"), Profit=("Profit", "sum"), Orders=("Order_ID", "count")
    ).reset_index()
    fig_scatter = px.scatter(sub_agg, x="Sales", y="Profit", size="Orders",
                              color="Category", text="Sub_Category",
                              color_discrete_map=CATEGORY_COLORS, size_max=35)
    fig_scatter.update_traces(textposition="top center", textfont=dict(size=10))
    fig_scatter.update_layout(**chart_layout, height=280,
                               xaxis=dict(showgrid=True, gridcolor="#F1F5F9"),
                               yaxis=dict(showgrid=True, gridcolor="#F1F5F9"))

    # ── Top Products ──
    top = d.groupby("Product")["Sales"].sum().nlargest(10).reset_index().sort_values("Sales")
    fig_top = px.bar(top, x="Sales", y="Product", orientation="h",
                     color="Sales", color_continuous_scale=["#DDD6FE", "#5B21B6"])
    fig_top.update_layout(**chart_layout, height=320, coloraxis_showscale=False,
                           xaxis=dict(showgrid=True, gridcolor="#F1F5F9"),
                           yaxis=dict(showgrid=False))

    # ── Discount vs Profit ──
    fig_disc = px.scatter(d, x="Discount", y="Profit", color="Category",
                           color_discrete_map=CATEGORY_COLORS,
                           hover_data=["Product", "Region"],
                           trendline="ols")
    fig_disc.update_layout(**chart_layout, height=320,
                            xaxis=dict(showgrid=True, gridcolor="#F1F5F9", tickformat=".0%"),
                            yaxis=dict(showgrid=True, gridcolor="#F1F5F9"))

    return kpis, fig_line, fig_pie, fig_bar, fig_scatter, fig_top, fig_disc


# ── Run ───────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    app.run(debug=True)
