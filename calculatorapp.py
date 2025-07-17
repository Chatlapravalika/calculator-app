import streamlit as st

st.title("🧮 Simple Calculator App")

num1 = st.number_input("Enter first number:")
num2 = st.number_input("Enter second number:")

operation = st.selectbox("Choose operation", ["Add", "Subtract", "Multiply", "Divide"])

if st.button("Calculate"):
    if operation == "Add":
        st.success(f"Result: {num1 + num2}")
    elif operation == "Subtract":
        st.success(f"Result: {num1 - num2}")
    elif operation == "Multiply":
        st.success(f"Result: {num1 * num2}")
    elif operation == "Divide":
        if num2 != 0:
            st.success(f"Result: {num1 / num2}")
        else:
            st.error("Cannot divide by zero!")
