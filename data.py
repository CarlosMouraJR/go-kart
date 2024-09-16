import pandas as pd
import streamlit as st


@st.cache_data
def get_data():
  try:
    df = st.session_state["df_kart"]
  except:
    df = load_data()

  df["Pista"] = df["Pista"].apply(str)
  df["Posição"] = df["Posição"].replace('NT', 0)
  df["Temporada"] = df["Temporada"].apply(str)

  df = df[df["Posição"] > 0]

  return df

def load_data():
  data = pd.read_excel("kart.xlsx", index_col=None)
  st.session_state["df_kart"] = data

  return data
