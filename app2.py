import streamlit as st
import seaborn as sns 



# Chargement des ensemble de données

tips = sns.load_dataset("tips")
titanic = sns.load_dataset('titanic')
iris = sns.load_dataset('iris')


# Option de la selection
datasets = {
    'Pourboire':tips,
    'Titanic':titanic,
    'Iris':iris
}

# Sidebar
st.sidebar.title('Selectionez un ensembled de données')
selected_dataset = st.sidebar.selectbox('', list(datasets.keys()))

# Affichage des information selectionnées
st.write('### Information sur l\'ensemble des données séléctionnées')
st.write(datasets[selected_dataset].head())


