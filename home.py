import streamlit as st

from helper import set_current_season
from data import get_data
from config import config_page
from season_stats import build_stats


config_page(st)
df = get_data()
df = set_current_season(df)

st.markdown("<h2>Temporada Atual</h2>", unsafe_allow_html=True)
build_stats(st, df)
