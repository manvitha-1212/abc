# -*- coding: utf-8 -*-
"""streamlitipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RK-KW5dTka88tTpx4dvrX2aIyIKwunOA
"""



import streamlit as st 
import joblib 
import numpy as np

from PIL import Image

st.title("MY FIRST STREAMLIT WEBAPP")


reload_model = joblib.load('happiness_model')

GDP_per_capita= st.number_input('GDP_per_capita')
Social_support = st.number_input('Social_support') 
Healthy_life_expectancy= st.number_input("Healthy_life_expectancy") 
Freedom_to_make_life_choices= st.number_input('Freedom_to_make_life_choices')
Generosity = st.number_input('Generosity') 
Perceptions_of_corruption= st.number_input("Perceptions_of_corruption") 
result =""

if st.button("Predict"): 
    prediction=reload_model.predict([[GDP_per_capita,Social_support, Healthy_life_expectancy,Freedom_to_make_life_choices,Generosity,Perceptions_of_corruption]])
    st.text('score')
    st.text(prediction)



