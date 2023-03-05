import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

st.title("Streamlit Option Menu")

# 1. as sidebar menu
# with st.sidebar:
#     selected = option_menu(
#         menu_title="Main menu", #required
#         options=["Home", "Projects", "Contact"], 
#         icons=["house", "book", "envelope"],
#         menu_icon="cast",
#         default_index=0,
#     ), 
with st.sidebar:
     selected = option_menu(
        menu_title=None, #required
        options=["Home", "Projects", "Contact"], 
        icons=["house", "book", "envelope"],
        menu_icon="cast",
        default_index=1,
        #orientation="horizontal",
        styles={
         "container": {"padding": "0!important", "background-color": "#fafafa"},
         "icon": {"color": "orange", "font-size": "25px"}, 
         "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
         "nav-link-selected": {"background-color": "green"},
     }
    )

if selected == "Home":
    st.header("Une carte")
    df = pd.read_csv("cities.csv").head(100)
    #st.write(df.head(10))
    st.map(df[['latitude', 'longitude']])

if selected == "Projects":
    st.title(f"You have selected {selected}")
if selected == "Contact":
    st.title(f"You have selected {selected}")        