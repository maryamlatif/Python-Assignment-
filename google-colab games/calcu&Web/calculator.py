import streamlit as st

st.title("💪 BMI Calculator")

height = st.number_input("Enter your height in meters:")
weight = st.number_input("Enter your weight in kg:")

if height > 0 and weight > 0:
    bmi = weight / (height ** 2)
    st.write(f"Your BMI is {bmi:.2f}")

    if bmi < 18.5:
        st.warning("Underweight")
    elif bmi < 25:
        st.success("Normal weight")
    elif bmi < 30:
        st.info("Overweight")
    else:
        st.error("Obese")
