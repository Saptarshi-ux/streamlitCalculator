import streamlit as st

# Title of the app
st.title("Calculator")

# Number inputs
num1 = st.number_input("Enter the number 1")
num2 = st.number_input("Enter the number 2")

# Operation selection
selection = st.selectbox("Select", ['Add', 'Subtract', 'Multiplication', 'Division'])
result = None
# Button to calculate
if st.button("Submit"):
    if selection == 'Add':
        result = num1 + num2
    elif selection == 'Subtract':
        result = num1 - num2
    elif selection == 'Multiplication':
        result = num1 * num2
    elif selection == 'Division':
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("Division by zero is not allowed!")
if result is not None:
    st.success(f"Result: {result}")
