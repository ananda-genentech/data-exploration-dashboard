import streamlit as st

def tests_tab():
    st.title('HOV Tests')
    st.write("\n")
    st.write("#### The following information is based on the paper, `A Monte Carlo Study of Seven Homogeneity of Variance Tests`. To conduct the Monte Carlo experiment there were repeated random sampling of data of different sizes and distributions to obtain results of power and robustness for each test")
    st.write("\n")
    st.write("## Background")
    st.write("\n")
    col1, col2, col3 = st.columns([3,.5,4])
    with col1:
        st.subheader("What is Power?")
        st.write("Power refers to the ability of a statistical test to detect a significant difference when one exists. The greater the number of unequal variances that are correctly detected by the test, the higher its power. An example of a power statistical test is t-test for sample means. It can detect even the slightest differences of mean between samples. ")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.subheader("What is Kurtosis?")
        st.write("`Kurtosis` is a measure to differentiate between two distributions with the same standard deviation and mean but different visually at the peaks and tails")
        st.image('./pages/hov/images/kurtosis.png')
        st.write("\n")
        st.write("\n")
        st.subheader("What is skew and what are the types of skew?")
        st.write("Skew determines how asymmetrical a distribution is. Negative (left) skew is when the tail is pointing to the left. Positive (right) skew is when the tail is pointing to the right. The distance of the central tendencies increases as the skew becomes greater. When there is no skew, the mean, median, and mode are equal. With a positive (right) skew, the mean is greater than the median, which is greater than the mode. On the other hand, with a negative (left) skew, the mode is greater than the median, which is greater than the mean. Skew with an absolute value less than .5 is considered symmetrical or no skew. Skew with an absolute value between .5 and 1 is considered moderately skewed. And skew with an absolute value greater than 1 is considered highly skewed.")
    

    with col2:
        pass

    with col3:
        st.subheader("What is Robustness")
        st.write("Robustness refers to the ability of a statistical test to produce valid results even in the presence of outliers or violations of assumptions. The more robust a test is, the less sensitive it is to these changes or violations. The greater the robustness, the fewer Type 1 errors (claims unequal variances when variances are equal) a test will make. An example of a robust statistical test is linear regression. Linear regression assumes normality but can still produce valid results when normality is violated. ")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.subheader("What are the Types of Distribution Based on Kurtosis?")
        st.write("``Leptokurtic`` distributions have kurtosis values higher than 3, with longer tails and are likely to have more prominent peaks. `Mesokurtic` distributions, also known as normal distributions, have a kurtosis value of 3. `Platykurtic` distributions have kurtosis values lower than 3, with shorter tails and are likely to have broader shoulders")
        st.image('./pages/hov/images/kurtosisTypes.png')

        st.write("\n")
        st.write("\n")
        st.write('#### Types of Skew')
        st.image('./pages/hov/images/skewTypes.png')
    
    

    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("## Monte Carlo Results")
    
    st.markdown("<h3 style='text-align: center;'>Large Sample Size (n=30)</h3>", unsafe_allow_html=True)
    st.write("\n")
    st.write("\n")
    st.write("\n")
   
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write('#### Robustness')
        st.write("* **most robust on average**: `Brown-Forsythe`")
        st.write("* **most robust when normal**: `Samiuddin cube`")
        st.write("* **most robust when leptokurtic**: `Z-VAR: Over-wood`")
        st.write("* **most robust when platykurtic**: `Z-VAR original`")
        st.write("* **most robust when moderate skew**: `Brown-Forsythe`")
        st.write("* **most robust when high skew**: `Brown-Forsythe`")

    with col2:
        st.write('#### Power')
        st.write("* **most power on average**: `Levene`")
        st.write("* **most power when normal**: `Samiuddin cube`")
        st.write("* **most power when leptokurtic**: `Z-VAR: original` or `Hartley FMAX` or `Samiuddin cube`")
        st.write("* **most power when platykurtic**: `Z-VAR: Over-wood`")
        st.write("* **most power when moderate skew**: `Z-VAR Original`")
        st.write("* **most power when high skew**: `Hartley FMAX`")

    with col3:
        st.write('#### Robustness and Power')
        st.write("* **most robust and power on average**: `Levene`")
        st.write("* **most robust and power when normal**: `Samiuddin cube`")
        st.write("* **most robust and power when leptokurtic**: `Hartley FMAX` and `Z-VAR: Over-wood`")
        st.write("* **most robust and power when platykurtic**: `Z-VAR: Over-wood`")
        st.write("* **most robust and power when moderate skew**: `Brown-Forsythe`")
        st.write("* **most robust and power when high skew**: `Hartley FMAX`")

    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.markdown("<h3 style='text-align: center;'>Small Sample Size (n=10)</h3>", unsafe_allow_html=True)
    st.write("\n")
    st.write("\n")
    st.write("\n")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write('#### Robustness')
        st.write("* **most robust on average**: `Brown-Forsythe`")
        st.write("* **most robust when normal**: `Z-VAR original`")
        st.write("* **most robust when leptokurtic**: `O'Brien`")
        st.write("* **most robust when platykurtic**: `Z-VAR original`")
        st.write("* **most robust when moderate skew**: `Brown-Forsythe`")
        st.write("* **most robust when high skew**: `Brown-Forsythe`")

    with col2:
        st.write('#### Power')
        st.write("* **most power on average**: `Z-VAR original`")
        st.write("* **most power when normal**: `Samiuddin cube`")
        st.write("* **most power when leptokurtic**: `Hartley FMAX`")
        st.write("* **most power when platykurtic**: `Brown-Forsythe`")
        st.write("* **most power when moderate skew**: `Z-VAR Original`")
        st.write("* **most power when high skew**: `Z-VAR Original`")

    with col3:
        st.write('#### Robustness and Power')
        st.write("* **most robust and power on average**: `Brown-Forsythe`")
        st.write("* **most robust and power when normal**: `Z-VAR Original`")
        st.write("* **most robust and power when leptokurtic**: `Hartley FMAX`")
        st.write("* **most robust and power when platykurtic**: `Brown-Forsythe`")
        st.write("* **most robust and power when moderate skew**: `Samiuddin cube`")
        st.write("* **most robust and power when high skew**: any test")