import streamlit as st

from data import get_data
from config import config_page
from season_stats import build_stats


config_page(st)
df = get_data()

seasons = df["Temporada"].value_counts().index
season = st.selectbox("Temporada", seasons)
df_filtered = df[df["Temporada"] == season]

build_stats(st, df_filtered)
