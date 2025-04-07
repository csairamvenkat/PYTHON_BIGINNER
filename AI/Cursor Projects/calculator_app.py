import streamlit as st

def calculate(num1, num2, operation):
    if operation == "Addition":
        return num1 + num2
    elif operation == "Subtraction":
        return num1 - num2
    elif operation == "Multiplication":
        return num1 * num2
    elif operation == "Division":
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    elif operation == "Power":
        return num1 ** num2
    else:
        return "Invalid operation"

def main():
    st.title("Simple Calculator App")
    st.write("Enter two numbers and select an operation")
    
    # Input fields
    num1 = st.number_input("First Number", step=0.1)
    num2 = st.number_input("Second Number", step=0.1)
    
    # Operation selection
    operation = st.selectbox(
        "Select Operation",
        ["Addition", "Subtraction", "Multiplication", "Division", "Power"]
    )
    
    # Calculate button
    if st.button("Calculate"):
        result = calculate(num1, num2, operation)
        st.success(f"Result: {result}")
        
    # History section
    with st.expander("Calculation History"):
        st.write("History will be shown here in future versions")
    
    # About section
    with st.expander("About"):
        st.write("""
        This is a simple calculator app built with Streamlit.
        It supports basic mathematical operations.
        """)

if __name__ == "__main__":
    main() 