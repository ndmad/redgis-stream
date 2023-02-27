import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Application de Distribution normale")
st.subheader("Auteur : Mamadou NDIAYE")
st.write(
    ("Cette application permet d'afficher l'histogramme d'une distribution normale."
     " L'utilisateur a la possibilité de varier le nombre de bins de l'histogramme"
     " et de donner un titre au graphique.")
)
data = np.random.normal(size=1000)
data = pd.DataFrame(data, columns=["Dist_norm"])
st.write(data.head())

fig, ax = plt.subplots()
n_bins = st.number_input(
    label='Choisis un nombre de bins',
    min_value= 10,
    value=20
)
ax.hist(data.Dist_norm, bins=n_bins)
graph_title = st.text_input(
    label="Ecris le titre du graphique"
)
plt.title(graph_title)
st.pyplot(fig)