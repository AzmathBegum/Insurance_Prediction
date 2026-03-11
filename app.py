import streamlit as st
from src.prediction import Insurance_Prediction

st.title('Insurance prediction')
st.write('Descriptionn about youre project')

Age=st.number_input('enter age:')
Annual_Income_LPA=st.number_input('enter Annual_Income_LPA:')
Policy_Term_Years=st.number_input('enter Policy_Term_Years:')
Sum_Assured_Lakhs=st.number_input('enter Sum_Assured_Lakhs:')

if st.button('predict'):
    model=Insurance_Prediction()
    result=model.prediction(Age,Annual_Income_LPA,Policy_Term_Years,Sum_Assured_Lakhs)
    st.success(result)