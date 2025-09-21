import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="TrendShop Dashboard", layout="wide")

st.title("📊 TrendShop Digital Dashboard (Jul - Sept)")

# ---- KPI Metrics ----
col1, col2, col3, col4 = st.columns(4)
col1.metric("Conversion Rate", "3.2%", "↑ 0.5%")
col2.metric("Website Traffic", "12,450", "↑ 8%")
col3.metric("New Customers", "1,240", "↑ 12%")
col4.metric("NPS Score", "68", "↑ 4")

# ---- Conversion Rate Trend ----
st.subheader("📈 Conversion Rate Trend")
df_conv = pd.DataFrame({
    "Month": ["July", "August", "September"],
    "Conversion Rate": [2.7, 3.0, 3.2]
})
line_chart = alt.Chart(df_conv).mark_line(point=True).encode(
    x="Month",
    y="Conversion Rate"
)
st.altair_chart(line_chart, use_container_width=True)

# ---- Traffic Sources ----
st.subheader("🌐 Website Traffic by Source")
df_traffic = pd.DataFrame({
    "Month": ["July", "July", "July", "August", "August", "August", "September", "September", "September"],
    "Source": ["Organic", "Paid", "Social", "Organic", "Paid", "Social", "Organic", "Paid", "Social"],
    "Visitors": [4000, 2500, 1500, 4200, 2700, 1600, 4600, 3000, 1800]
})
area_chart = alt.Chart(df_traffic).mark_area().encode(
    x="Month",
    y="Visitors",
    color="Source"
)
st.altair_chart(area_chart, use_container_width=True)

# ---- New vs Returning Customers ----
st.subheader("👥 New vs Returning Customers")
df_customers = pd.DataFrame({
    "Month": ["July", "July", "August", "August", "September", "September"],
    "Type": ["New", "Returning", "New", "Returning", "New", "Returning"],
    "Count": [700, 300, 800, 350, 900, 400]
})
bar_chart = alt.Chart(df_customers).mark_bar().encode(
    x="Month",
    y="Count",
    color="Type"
)
st.altair_chart(bar_chart, use_container_width=True)

# ---- Customer Feedback ----
st.subheader("💬 Customer Feedback")
feedback = pd.DataFrame({
    "Date": ["2025-07-12", "2025-08-05", "2025-09-14"],
    "Customer": ["Alicia", "Brandon", "Chong"],
    "Feedback": [
        "Loved the fast delivery!",
        "Product quality could be better.",
        "Excellent support and return process."
    ]
})
st.table(feedback)
