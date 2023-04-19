import streamlit as st

def find_largest(n1, n2, n3):
    largest = n1
    if n2 > largest:
        largest = n2
    if n3 > largest:
        largest = n3
    return largest

st.title("Find the Largest Number")
num1 = st.number_input("Enter the first number:")
num2 = st.number_input("Enter the second number:")
num3 = st.number_input("Enter the third number:")

if st.button("Find Largest"):
    large = find_largest(num1, num2, num3)
    st.write("The largest number is:", large)
