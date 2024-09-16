import pandas as pd
import streamlit as st

from data import get_data
from config import config_page
from helper import build_card_stats_content, set_columns_view
from season_stats import build_stats
import plotly.express as px


config_page(st)
df = get_data()

pilots = df["Corredor"].sort_values().unique()
pilot = st.selectbox("Corredor", pilots)

df_filtered = df[df["Corredor"] == pilot].sort_values(by=["Data", "Tempo"])
df_filtered['t_Tempo'] = df_filtered['Tempo']
df_filtered['Tempo'] = pd.to_timedelta(df_filtered['Tempo'])

show_table = df_filtered
show_table["Tempo"] = show_table["t_Tempo"]
show_table = show_table.drop(columns=["t_Tempo"])

st.write("Informações Gerais:")
st.write(show_table)

fig = px.line(df_filtered, x="Data", y="Tempo", text="t_Tempo")

fig.update_xaxes(range=[df_filtered["Data"].min() - pd.Timedelta(days=50),
                        df_filtered["Data"].max() + pd.Timedelta(days=30)])

min_tempo = df_filtered['Tempo'].min() - pd.Timedelta(seconds=10)
max_tempo = df_filtered['Tempo'].max() + pd.Timedelta(seconds=10)

# Exibir o gráfico
fig.update_yaxes(tickvals=df_filtered['Tempo'].unique(),
                 ticktext=df_filtered['t_Tempo'])

fig.update_traces(textposition="bottom left")

# card 1
menor_tempo = df_filtered["Tempo"].min().split("00:")[1]
nome_menor_tempo = df_filtered[df_filtered["Tempo"] == menor_tempo]["Corrida"]

# card 2
menor_tempo_volta = df_filtered["Tempo melhor volta"].min()
nome_menor_tempo_volta = df_filtered[df_filtered["Tempo melhor volta"] == menor_tempo_volta]["Corrida"]

# card 3
melhor_posicao = df_filtered["Posição"].min()

# ------------- view -------------

st.write("Tempos Corridas:")
st.write(fig)

# Cards
grid = set_columns_view(st)

with grid[0]:
  build_card_stats_content(st, "Menor tempo 🕐", menor_tempo, None)

with grid[1]:
  build_card_stats_content(st, "Melhor tempo volta 🚀", menor_tempo_volta, None)

with grid[2]:
  build_card_stats_content(st, "Melhor posição 🏆", melhor_posicao, None)
