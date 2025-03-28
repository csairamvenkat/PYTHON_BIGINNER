import streamlit as st
import pandas as pd
import numpy as np  # If you're working with NumPy arrays

def display_array_as_table(data, columns=None):
    """Displays a Python list, NumPy array, or Pandas DataFrame as a table in Streamlit."""

    if isinstance(data, list):
        # Convert list to DataFrame
        if isinstance(data[0], list) or isinstance(data[0], tuple) : # Check for list of lists
            df = pd.DataFrame(data, columns=columns) if columns else pd.DataFrame(data)
        else: # Handle 1D list
             df=pd.DataFrame(data, columns=["Value"]) if columns is None else pd.DataFrame(data, columns=columns)

    elif isinstance(data, np.ndarray):
        # Convert NumPy array to DataFrame
        df = pd.DataFrame(data, columns=columns) if columns is not None else pd.DataFrame(data)

    elif isinstance(data, pd.DataFrame):
        df = data  # Data is already a DataFrame

    else:
        st.error("Unsupported data type. Please provide a list, NumPy array, or Pandas DataFrame.")
        return  # Exit the function if the data type is not supported

    # Display the DataFrame as a table
    st.dataframe(df) # Or st.table(df) for a static table.  dataframe is preferred for interactivity

    # Optional: Add download button
    st.download_button(
        label="Download data as CSV",
        data=df.to_csv(index=False).encode('utf-8'),
        file_name="data.csv",
        mime="text/csv",
        key=np.random.rand(1, 100)
    )



def main():
    st.title("Display Array as Table")

    # Example 1: List of lists
    st.subheader("Example 1: List of Lists")
    my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    display_array_as_table(my_list, columns=["Col1", "Col2", "Col3"]) #Provide column names

    # Example 2: 1D List
    st.subheader("Example 2: 1D List")
    my_1d_list = [10,20,30,40,50]
    display_array_as_table(my_1d_list, columns=["Values"],) #Provide column names

    # Example 3: NumPy Array
    st.subheader("Example 3: NumPy Array")
    my_array = np.array([[10, 20], [30, 40], [50, 60]])
    display_array_as_table(my_array, columns=["A", "B"]) #Provide column names

    # Example 4: Pandas DataFrame (just for completeness)
    st.subheader("Example 4: Pandas DataFrame")
    my_dataframe = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Age': [25, 30]})
    display_array_as_table(my_dataframe)  # No need for columns here as it's already a DataFrame

if __name__ == "__main__":
    main()