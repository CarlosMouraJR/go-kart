def config_page(st):
  st.set_page_config(
    # layout="wide",
    page_title="Kart Statics"
  )

  st.sidebar.page_link("home.py", label="Temporada Atual")
  st.sidebar.page_link("pages/seasons.py", label="Todas as temporadas")
  st.sidebar.page_link("pages/pilots.py", label="Pilotos")
