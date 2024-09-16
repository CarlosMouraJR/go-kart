def points_value():
  return {
    1: 25,
    2: 18,
    3: 15,
    4: 12,
    5: 10,
    6: 8,
    7: 6,
    8: 4,
    9: 2,
    10: 1
  }

def set_current_season(df):
  current_season = df["Temporada"].max()
  return df[df["Temporada"] == df["Temporada"].max()]

def points_explanation():
  return '''
    O gráfico acima utiliza o sistema de pontos da Fórmula 1 para segmentar e visualizar o desempenho dos pilotos em cada corrida. Em cada etapa, os pilotos recebem pontos com base na sua posição final, de acordo com as regras da F1, que seguem a seguinte distribuição para os dez primeiros colocados:

    1º lugar: 25 pontos

    2º lugar: 18 pontos

    3º lugar: 15 pontos

    4º lugar: 12 pontos

    5º lugar: 10 pontos

    6º lugar: 8 pontos

    7º lugar: 6 pontos

    8º lugar: 4 pontos

    9º lugar: 2 pontos

    10º lugar: 1 ponto

    Além disso, um ponto extra é concedido ao piloto que fizer a volta mais rápida, desde que termine entre os dez primeiros colocados.
  '''

def set_columns_view(st):
  row1 = st.columns(3)

  return [col.container(height=300) for col in row1]

def build_card_stats_content(st, text, value, pilot=None):
  st.write(text)
  st.markdown("<h2>{}</h2>".format(value), unsafe_allow_html=True)
  if(pilot != None): st.markdown(''':green[{}]'''.format(pilot))

def add_extra_point(df):
  for corrida in df["Corrida"].unique():
    corrida_df = df[df["Corrida"] == corrida]

    top_10_df = corrida_df[corrida_df["Posição"] <= 10]

    if not top_10_df.empty:
      corredor_mais_rapido = top_10_df[top_10_df["Tempo"] == top_10_df["Tempo"].min()]["Corredor"].iloc[0]

      df.loc[(df["Corrida"] == corrida) & (df["Corredor"] == corredor_mais_rapido), "Pontos"] += 1

  return df
