import plotly.graph_objects as go

from helper import add_extra_point, build_card_stats_content, points_value, set_columns_view, points_explanation


def build_stats(st, df):
  df["Pontos"] = df["Posição"].map(points_value()).apply(lambda x: x)

  # Aplicar a função para adicionar ponto extra
  df = add_extra_point(df)

  # Calcular a pontuação total para cada corredor
  total_pontos = df.groupby("Corredor")["Pontos"].sum().reset_index(name="Pontos")

  # Pegar somente os 10 melhores
  top_10 = total_pontos.nlargest(10, "Pontos")

  # Ordenar pelo total de pontos em ordem decrescente e pegar os 10 primeiros
  top_10 = top_10.sort_values(by="Pontos", ascending=True)

  # Criar a lista de cores
  colors = ["gray"] * (len(top_10) - 3) + ["#FF00FF"] + ["#00FFFF"] + ["gold"]

  fig = go.Figure(go.Bar(
    x=top_10["Pontos"],
    y=top_10["Corredor"],
    orientation="h",
    marker=dict(color=colors)
  ))

  # card 1
  menor_tempo = df["Tempo"].min()

  nome_menor_tempo = df[df["Tempo"] == menor_tempo]["Corredor"].values[0]

  # card 2
  menor_tempo_volta = df["Tempo melhor volta"].min()
  nome_menor_tempo_volta = df[df["Tempo melhor volta"] == menor_tempo_volta]["Corredor"].values[0]

  # # card 3
  # maior_velocidade = df["Velocidade"].max()
  # nome_maior_velocidade = df[df["Velocidade"] == maior_velocidade]["Corredor"].values[0]
  # maior_velocidade = str(np.round(maior_velocidade, 2)) + "km/h"


  # ------------- view -------------

  fig.update_layout(title="Pontuação")
  # Main Chart
  st.plotly_chart(fig)

  with st.expander("Sistema de Pontos"):
    st.write(points_explanation())

  # Cards
  grid = set_columns_view(st)

  with grid[0]:
    build_card_stats_content(st, "Menor tempo 🕐", menor_tempo, nome_menor_tempo)

  with grid[1]:
    build_card_stats_content(st, "Melhor tempo volta 🚀", menor_tempo_volta, nome_menor_tempo_volta)

  # with grid[2]:
    # build_card_stats_content(st, "Maior Velocidade 🛞", maior_velocidade, nome_maior_velocidade)
