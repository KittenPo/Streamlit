# ===============================================================
#           CREATE DASHBOARD BIKE SHARING USING STREAMLIT       =
#           ---------------------------------------------       =
# Nama          : Rahadian Muhammad Sutandar                    =
# Email         : rahadiansutandar@gmail.com                    =
# Id Dicoding   : dicoding.com/users/rahadian_ms/               =
#                                                               =
# ===============================================================

# Import Library
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ==============================
# LOAD DATA
# ==============================

def load_data():
    data = pd.read_csv('main_data.csv')
    return data

data = load_data()

# ==============================
# TITLE DASHBOARD
# ==============================
# Set page title
st.title("Dashboard Kualitas Udara di Berbagai Stasiun di China Tahun 2013-2017 ")
# ==============================
# SIDEBAR
# ==============================
st.sidebar.title("Information:")
st.sidebar.markdown("**• Nama: Rahadian Muhammad Sutandar**")
st.sidebar.markdown(
    "**• Email: [rahadiansutandar@gmail.com](rahadiansutandar@gmail.com)**")
st.sidebar.markdown(
    "**• Dicoding: [Rahadian_Ms](https://www.dicoding.com/users/rahadian_ms/academies)**")
st.sidebar.markdown(
    "**• LinkedIn: [Rahadian Muhammad Sutandar](https://www.linkedin.com/in/rahadianms/)**")

# Display
df_airQ = data
average_pollution = df_airQ.groupby('station')[['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']].mean()
average_pollution['average_pollution'] = average_pollution.mean(axis=1).round(2)
average_pollution = average_pollution.reset_index()

fig1 = px.bar(average_pollution, x='station', y='average_pollution',
             title='Rata-rata Tingkat Polusi di Setiap Stasiun',
             labels={'average_pollution': 'Rata-rata Polusi'},
             color='average_pollution',
             color_continuous_scale='Viridis')

st.plotly_chart(fig1)

fig2 = px.scatter(df_airQ, x='TEMP', y='average_pollution', title='Hubungan Antara Suhu dan Rata-rata Polusi Udara',
                 labels={'TEMP': 'Suhu (°C)', 'average_pollution': 'Rata-rata Polusi'},
                 hover_data=['station'], color='station')
st.plotly_chart(fig2)

fig3 = px.scatter(df_airQ, x='RAIN', y='average_pollution', title='Hubungan Antara Hujan dan Rata-rata Polusi',
                 labels={'RAIN': 'Curah Hujan (mm)', 'average_pollution': 'Rata-rata Polusi'},
                 hover_data=['station'], color='station')

st.plotly_chart(fig3)
