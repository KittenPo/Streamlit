# ===============================================================
#           CREATE DASHBOARD BIKE SHARING USING STREAMLIT       =
#           ---------------------------------------------       =
# Nama          : Maulana Kavaldo                               =
# Email         : alkav.maulana@gmail.com                       =
# Id Dicoding   : dicoding.com/users/maulanakavaldo/            =
# Github Pages  : maulanakavaldo.github.io                      =
# Created       : 28 September 2023                             =
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
    data = pd.read_csv("C:\Users\rahad\Downloads\TubesFix\merged_dataset.csv")
    return data


data = load_data()

