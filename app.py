import streamlit as st
from src.prediction import Insurance_Prediction

st.title("Insurance Premium Prediction")
st.write("This app predicts the annual insurance premium based on customer details.")

# User Inputs
Age = st.number_input("Enter Age", min_value=18, max_value=100, step=1)
Annual_Income_LPA = st.number_input("Enter Annual Income (LPA)", min_value=0.0)
Policy_Term_Years = st.number_input("Enter Policy Term (Years)", min_value=1)
Sum_Assured_Lakhs = st.number_input("Enter Sum Assured (Lakhs)", min_value=1.0)

# Load model once
model = Insurance_Prediction()

# Prediction button
if st.button("Predict Premium"):
    result = model.prediction(Age, Annual_Income_LPA, Policy_Term_Years, Sum_Assured_Lakhs)
    st.success(f"Predicted Annual Premium: {result:.2f} Thousand")