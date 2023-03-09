import streamlit as st

def fundies_tab():
    st.title("Fundamentals")
    st.write("\n")
   
    col1, col2, col3, = st.columns([2.5,.5,4])
   
    with col1:

        st.subheader("What is Variance and Covariance?")

        st.write("**Variance** is a measure of how spread out the data values are from the mean on average. **Boxplots** are often used to visualize **variance** of a dataset. **Variance** is more statistically intuitive than range, which is sensitive to outliers.")
        st.image("./pages/hov/images/boxplot.png", )

        st.write("\n")
        st.write("\n")

        st.subheader("What is Homogeneity of Variance (HOV)?")

        st.write("Homogeneity of variance (HOV) aka homoscedasticity is when different groups within a covariate have equal variances. HOV must be tested and corrected before deploying a model that assumes homoscedasticity. Heteroscedasticity or heterogeneity of variances (HEV) is the opposite: different groups have different variances.")
        st.image("./pages/hov/images/hevboxplot.png")

    with col2: 
        pass
    
    with col3:
        st.subheader("What is Homogeneity?")
        
        st.write("Homogeneity can be understood as a state of sameness, equality, and similarity. There are various types of homogeneity, and two examples are homogeneous data points and homogeneous sampling.")
        st.write("Homogeneous data points share a common identifier that is being measured, resulting in data that is uniform and comparable. In contrast, heterogeneous data points measure different groups within a variable and may not be directly comparable. For example, when we examine the frequency plots, we can see that homogeneous data measures the same crime, while heterogeneous data measures different crimes.")
        st.write("Similarly, homogeneous sampling refers to a sample in which all groups of a variable have the same number of instances, resulting in a evenly representative sample. Conversely, a non-homogeneous sample has varying numbers of instances for each group, which can introduce biases and inaccuracies when comparing groups.")
        st.write("To illustrate this, consider the pie charts below. One pie chart has an even split of the variable, representing a homogeneous sample, while the other has a heterogeneous split, representing a non-homogeneous sample.")
        st.write("\n")
        st.write("\n")
        col1, col2, col3 = st.columns([4,1,4])

        with col1:
            st.markdown("<h5 style='text-align: center;'>Heterogeneity Data Points</h5>", unsafe_allow_html=True)
            st.write("\n")
            st.image("./pages/hov/images/hevfreqplot.png")
            st.write("\n")
            st.markdown("<h5 style='text-align: center;'>Heterogeneity Sampling</h5>", unsafe_allow_html=True)
            st.write("\n")
            st.write("\n")
            st.image("./pages/hov/images/hevpiechart.png", width=275)
            
            
        with col2:
          pass
      
        with col3:
            
            st.markdown("<h5 style='text-align: center;'>Homogeneity Data Points</h5>", unsafe_allow_html=True)
            st.write("\n")               
            st.image("./pages/hov/images/hovfreqplot.png")
            st.write("\n")    
            st.markdown("<h5 style='text-align: center;'>Homogeneity Sampling</h5>", unsafe_allow_html=True)
            st.write("\n")
            st.write("\n")   
            st.image("./pages/hov/images/hovpiechart.png", width=275)

        st.write("\n")
        st.write("\n")
        st.subheader("What is Homogeneity of Covariance (HOCV)?")


