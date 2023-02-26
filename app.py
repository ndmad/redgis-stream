import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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