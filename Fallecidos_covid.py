import streamlit as st
from streamlit_option_menu import option_menu


with st.sidebar:
    selected = option_menu(
        menu_title = 'Menu', 
        options = ['Inicio', 'Reportes', 'Equipo'],
        icons = ['house', 'book', 'people'],
        menu_icon='dog',
        default_index = 0,
    )
st.set_page_config(
    page_title="FALLECIDOS COVID",
    page_icon="👋",
)

st.write("#BIENVENIDOS! 👋")

st.sidebar.success("pagina a")

st.markdown(
    """
    Esta página se creo con la finalidad de visualizar la información sobre los fallecidos por covid en el Perú
    **👈}
    ### A
    - pagina 1
    - pagina 2

    ### B
    - P1
    - P2
    """
   
)

import streamlit as st
import time
import numpy as np

st.set_page_config(page_title="Plotting Demo", page_icon="📈")

st.markdown("# Plotting Demo")
st.sidebar.header("Plotting Demo")
st.write(
    """This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!"""
)

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows)

for i in range(1, 101):
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    status_text.text("%i%% Complete" % i)
    chart.add_rows(new_rows)
    progress_bar.progress(i)
    last_rows = new_rows
    time.sleep(0.05)

progress_bar.empty()
