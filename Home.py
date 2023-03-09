import streamlit as st
import os

# Define the path to the R installation directory
r_home = '/usr/local/bin/R'

# Set the R_HOME environment variable
os.environ['R_HOME'] = r_home

# Your Streamlit app code goes here


st.title("Comprehensive Guide to Exploratory Data Analysis")
