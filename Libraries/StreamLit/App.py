import streamlit as st

# Title
st.title("Hello, Streamlit! 🎈")

# Header and Subheader
st.header("This is a header")
st.subheader("This is a subheader")

# Text
st.write("This is a simple Streamlit app.")

# Input box
name = st.text_input("Enter your name:")
st.write(f"Hello, {name}!")

# Button
if st.button("Click Me"):
    st.success("You clicked the button!")

# Sidebar
st.sidebar.title("Sidebar Menu")
st.sidebar.write("You can add widgets here too.")

# Display an image
st.image("https://www.streamlit.io/images/brand/streamlit-mark-color.png", width=250)
