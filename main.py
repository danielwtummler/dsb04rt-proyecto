import streamlit as st

from page_app import page_app_func
from ml import ml
from eda import eda
from about import about_func

from modules.funciones_ml import PAGE_CONFIG

st.set_page_config(**PAGE_CONFIG)

def main():

    menu = ["Main App", "Exploratory Data Analysis", "Machine Learning Model", "About"]

    page = st.sidebar.selectbox(label = "Menu", options = menu)

    if page == "Main App":

        page_app_func()

    elif page == "Exploratory Data Analysis":
        
        eda()

    elif page == "Machine Learning Model":

        ml()

    else:

        about_func()

if __name__ == "__main__":
    main()