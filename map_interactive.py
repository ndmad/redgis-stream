import streamlit as st
import pandas as pd
import pydeck as pdk

# Titre de l'application
st.title("Carte interactive")

# Charger les données
data_url = (
    "https://raw.githubusercontent.com/visgl/deck.gl-data/master/website/bart-lines.json"
)
data = pd.read_json(data_url)

# Afficher les données brutes
st.write("Voici les données brutes (JSON) :")
st.write(data)

# Afficher les données sous forme de carte interactive
st.write("Voici une carte interactive :")

# Définir la vue de la carte
view_state = pdk.ViewState(
    longitude=-122.4,
    latitude=37.76,
    zoom=11,
    pitch=50,
)

# Définir les couches de la carte
layer = pdk.Layer(
    "PathLayer",
    data=data,
    get_color=[255, 165, 0],
    width_scale=20,
    width_min_pixels=2,
    get_path="path",
    get_width="width",
)

# Afficher la carte
r = pdk.Deck(
    layers=[layer],
    initial_view_state=view_state,
    map_style="mapbox://styles/mapbox/light-v9",
)
st.pydeck_chart(r)
