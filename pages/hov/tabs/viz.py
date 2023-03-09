import streamlit as st
from pages.hov.functions.visuals import stCondBoxPlot, stCondCleveland
import pandas as pd

def viz_tab():
    st.title("Visualizations")
    st.write("\n")
    st.write("On this page, you can upload a csv file that can be used to visualize if your dataset contains HOV or HOCV. Once you upload the CSV file dropdowns will appear that will allow you to customize your visualizations")
    # Get the CSV file from user input
    st.subheader("Upload CSV to Visualize If Your Data is HOV vs HEV")
    csv_file = st.file_uploader("", type="csv")
    st.write("\n")
    st.write("\n")
    st.write("\n")

    if csv_file is not None:
        # Load the CSV data into a Pandas dataframe
        df = pd.read_csv(csv_file)

        # Get the list of column names
        columns = list(df.columns)
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.subheader(f"Here are the first 5 rows of your data")
        st.write(df.head())


        st.write("\n")
        st.write("\n")
        st.write("\n")

        st.subheader("Customize Your Visualizations")

        # Ask the user to select a column
        col1, col2, col3 = st.columns(3)

        # Add a selection dropdown in each column for the corresponding variable
        with col1:
            numVar = st.selectbox("Select a column for the Numerical Variable", columns, key='num')
                

        with col2:
            groupVar = st.selectbox("Select a column for the Conditional (Categorical) Variable", columns, key='cond')
            

        with col3:
            colorVar = st.selectbox("Select a column for the Color (Categorical) Variable", columns, key='color')

        col1, col2 = st.columns(2)

        # Add a selection dropdown in each column for the corresponding variable
        with col1:
            boxTitle = st.text_input('Write a title for the Conditional Boxplot', '')
                

        with col2:
            cleveTitle = title = st.text_input('Write a title for the Cleveland DotPlot', '')
    
    button = st.button('Submit Variables', key='viz')

    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    
    col1, col2 = st.columns(2)
   
    with col1:
        st.subheader("Conditional Boxplot")

        condBoxPlot = '''def condBoxPlot(df, xCol, yCol, title):
    
    # Create a conditional boxplot based on emotion and priming
    fig = px.box(df, x=xCol, y=yCol, color='Emotion State')

    # Update the layout
    fig.update_layout(title=title, xaxis_title=xCol, yaxis_title=yCol)

    # Show the plot
    fig.show()'''
        
        st.code(condBoxPlot, language='python')
        if csv_file is not None:
            if button:
                stCondBoxPlot(df, groupVar, numVar, colorVar, boxTitle )
            
    
 

    with col2:
        st.subheader("Conditional Cleveland Dot Plot")
        

        condCleveland = '''def condCleveland(df, xCol, yCol, zCol, title):
    
    # Create a conditional Cleveland dot plot based on emotion and priming
    fig = px.strip(df, x=xCol, y=yCol, color=zCol, orientation="v")

    # Update the layout
    fig.update_layout(title=title, xaxis_title=xCol, yaxis_title=yCol)

    # Show the plot
    fig.show()'''
        
        st.code(condCleveland, language='python')

        if csv_file is not None:
            if button:
                stCondCleveland(df, groupVar, numVar, colorVar, cleveTitle )
        
