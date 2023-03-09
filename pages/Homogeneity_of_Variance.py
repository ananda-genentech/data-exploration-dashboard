import streamlit as st
import pandas as pd
from pages.hov.tabs.fundies import fundies_tab
from pages.hov.tabs.viz import viz_tab
from pages.hov.tabs.hovtests import tests_tab
from pages.hov.tabs.premodel import premodel_tab

st.set_page_config(layout="wide")
st.title('Homogeneity of Variance (HOV)')

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs(["Fundamentals", "Importance", "Visualizations",                                                                
                                                                "Tests", "Testing Pre-Model", "Testing Post-Model",                                                                 
                                                                "Impact", "Handling Violations", "Alternatives"])

with tab1:
    fundies_tab()

with tab2:
    pass


with tab3:
    viz_tab()

with tab4:
    tests_tab()

with tab5:
    premodel_tab()

