import streamlit as st

st.sidebar.title("Navigation")

page = st.sidebar.radio("Go to", ("Home", "Data", "Analysis", "Settings","Tabular Page"))

if page == "Home":
    st.title("Home Page")
    st.write("Welcome to the home page!")
    # Home page content

elif page == "Data":
    st.title("Data Page")
    st.write("Here's your data:")
    # Data page content, e.g., display a dataframe
    import pandas as pd
    df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
    st.dataframe(df)

elif page == "Analysis":
    st.title("Analysis Page")
    st.write("Performing analysis...")
    # Analysis page content, e.g., plots, calculations
    import matplotlib.pyplot as plt
    plt.plot([1, 2, 3], [4, 5, 6])
    st.pyplot(plt)

elif page == "Settings":
    st.title("Settings Page")
    st.write("Configure your settings here.")
    # Settings page content, e.g., form inputs
    option = st.selectbox('Select an option', ['A', 'B', 'C'])
    st.write('You selected:', option)
elif page=="Tabular Page":
    import streamlit as st

st.title("My Streamlit App")

with st.expander("Section 1: Data Input"):
    st.write("Enter your data here:")
    # Input elements

with st.expander("Section 2: Data Visualization"):
    st.write("Charts and graphs go here:")
    # Plots

with st.expander("Section 3: Analysis Results"):
    st.write("Results of your analysis:")
    # Output