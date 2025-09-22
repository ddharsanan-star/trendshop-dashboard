import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="TrendShop Dashboard", layout="wide")

st.title("📊 TrendShop Digital Dashboard (Jul - Sept)")

# ---- 1. KPI Metrics ----
col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Kadar Penukaran", "5%", "↔")
col2.metric("Pelawat Laman Web", 6000+5000+4000+0, "↑ 25%")
col3.metric("Pelanggan Baru", 500, "↑ 11%")
col4.metric("NPS Score", 6, "↓ 2")
col5.metric("AOV (RM)", 100, "↔ 100")

# ---- 2. Conversion Rate Trend ----
st.subheader("📈 Kadar Penukaran Trend")
df_conv = pd.DataFrame({
    "Bulan": ["Julai", "Ogos", "Sept"],
    "Pelawat": [1000, 12000, 15000],
    "Pembelian": [500, 600, 750],
    "Kadar Penukaran (%)": [3, 5, 7]
})
line_chart = alt.Chart(df_conv).mark_line(point=True).encode(
    x="Bulan",
    y=alt.Y("Kadar Penukaran (%)", scale=alt.Scale(domain=[0, 10])),
    tooltip=["Bulan", "Pelawat", "Pembelian", "Kadar Penukaran (%)"]
).interactive()
st.altair_chart(line_chart, use_container_width=True)

# ---- 3. Traffic Sources ----
st.subheader("🌐 Trafik Laman Web Mengikut Sumber")
df_traffic = pd.DataFrame({
    "Bulan": ["Julai","Julai","Julai","Julai",
              "Ogos","Ogos","Ogos","Ogos",
              "Sept","Sept","Sept","Sept"],
    "Sumber": ["Organik","Berbayar","Media Sosial","Rujukan",
               "Organik","Berbayar","Media Sosial","Rujukan",
               "Organik","Berbayar","Media Sosial","Rujukan"],
    "Pelawat": [4000,3000,3000,0,
                5000,4000,3000,0,
                6000,5000,4000,0]
})
area_chart = alt.Chart(df_traffic).mark_area(opacity=0.6).encode(
    x="Bulan",
    y="Pelawat",
    color="Sumber",
    tooltip=["Bulan", "Sumber", "Pelawat"]
).interactive()
st.altair_chart(area_chart, use_container_width=True)

# ---- 4. New vs Returning Customers ----
st.subheader("👥 Pelanggan Baru vs Pelanggan Kembali")
df_customers = pd.DataFrame({
    "Bulan": ["Julai","Julai","Ogos","Ogos","Sept","Sept"],
    "Jenis": ["Baru","Kembali","Baru","Kembali","Baru","Kembali"],
    "Jumlah": [400,100,450,150,500,250]
})
bar_chart = alt.Chart(df_customers).mark_bar().encode(
    x="Bulan",
    y="Jumlah",
    color="Jenis",
    tooltip=["Bulan", "Jenis", "Jumlah"]
)
st.altair_chart(bar_chart, use_container_width=True)

# ---- 5. NPS Feedback ----
st.subheader("💬 Maklum Balas Pelanggan (NPS)")
df_nps = pd.DataFrame({
    "Bulan": ["Julai","Ogos","Sept"],
    "NPS": [7,8,6],
    "Maklum Balas": [
        "Baik tetapi perlu penambahbaikan",
        "Servis pelanggan sangat baik",
        "Penghantaran lambat"
    ]
})
st.table(df_nps)

# ---- 6. AOV Trend ----
st.subheader("💰 Purata Nilai Pesanan (AOV)")
df_aov = pd.DataFrame({
    "Bulan": ["Julai","Ogos","Sept"],
    "Jumlah Jualan (RM)": [50000,60000,75000],
    "Jumlah Pembelian": [500,600,750],
    "AOV (RM)": [100,100,100]
})
aov_chart = alt.Chart(df_aov).mark_line(point=True, color="green").encode(
    x="Bulan",
    y="AOV (RM)",
    tooltip=["Bulan", "Jumlah Jualan (RM)", "Jumlah Pembelian", "AOV (RM)"]
).interactive()
st.altair_chart(aov_chart, use_container_width=True)
