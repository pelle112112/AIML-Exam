import streamlit as st
from st_pages import add_page_title, get_nav_from_toml
import pandas as pd
import numpy as np
import os

st.set_page_config( layout='wide')
currentDir = os.getcwd()
toml_path = os.path.join(currentDir, "Webapp", "pages_sections.toml")

st.title('Resume Screening Tool')

nav = get_nav_from_toml("pages_sections.toml")
if nav:
    pg = st.navigation(nav)
    #add_page_title(pg)
    pg.run()
else:
    st.write("No pages to show")