import streamlit as st
import pandas as pd
from pages.hov.functions.framework import chooseHOVTest

def premodel_tab():
    st.title("Testing for HOV Before Model Deployment")
    st.write("\n")
    # Get the CSV file from user input
    st.subheader("Upload CSV to Test Which Raw Data Variables are HOV vs HEV")
    csv_file = st.file_uploader("Upload CSV", type="csv", key='premodel')

    if csv_file is not None:
        # Load the CSV data into a Pandas dataframe
        df = pd.read_csv(csv_file)
        columns = list(df.columns)

        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.subheader(f"Here are the first 5 rows of your data")
        st.write(df.head())


        st.write("\n")
        st.write("\n")
        st.write("\n")

        st.subheader("Customize your HOV Test")
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            groupVar = st.selectbox("Select a column for the Categorical Variable", columns)

        with col2: 
            numVar = st.selectbox("Select a column for the Numerical Variable", columns)

        with col3:
            alphaDist = st.selectbox("Choose an alpha value for the Distribution Test", [.01, .05])
        
        with col4:
            alphaHOV = st.selectbox("Choose an alpha value for the HOV Test", [.01, .05])

        button = st.button('Submit Variables', key='test')
        
        if button:
            result, feats = chooseHOVTest(df, groupVar, numVar, alphaDist, alphaHOV)
            
            st.write("\n")
            st.write("\n")
            st.write("\n")
            st.subheader("Test Results and Variable Features")
            col1, col2= st.columns(2)

            with col1:
                
                st.write(result)

            with col2:
                st.write(feats)