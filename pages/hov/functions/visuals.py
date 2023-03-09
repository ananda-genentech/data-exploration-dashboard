import plotly.express as px
import streamlit as st

def stCondBoxPlot(df, xCol, yCol, zCol, title):
    
    # Create a conditional boxplot based on emotion and priming
    fig = px.box(df, x=xCol, y=yCol, color=zCol)

    # Update the layout
    fig.update_layout(title=title, xaxis_title=xCol, yaxis_title=yCol)

    # Display the plot in Streamlit using Plotly's built-in Streamlit support
    st.plotly_chart(fig)

def stCondCleveland(df, xCol, yCol, zCol, title):
    
    # Create a conditional Cleveland dot plot based on emotion and priming
    fig = px.strip(df, x=xCol, y=yCol, color=zCol, orientation="v")

    # Update the layout
    fig.update_layout(title=title, xaxis_title=xCol, yaxis_title=yCol)

    # Display the plot in Streamlit using Plotly's built-in Streamlit support
    st.plotly_chart(fig)
