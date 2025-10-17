import streamlit as st
import pandas as pd
import pickle
import numpy as np

model = pickle.load(open("model/model_final.pkl","rb"))


st.header("Iris App")
# st.text_input('Sepal length')
# st.text_input('Sepal width')
# st.text_input('petal length')
# st.text_input('petal width')
# st.button('submit')

with st.form("Iris app form"):
    pl = st.number_input('Enter Petal length')
    pw = st.number_input('Enter Petal width')
    sl = st.number_input('Enter Sepal length')
    sw = st.number_input('Enter Sepal width')
    submitted = st.form_submit_button('Submit')
    if submitted:
        prediction = model.predict([[pl,pw,sl,sw]])
        # st.success(f"Predicted species: {prediction[0]}")

        species_map = {0: "Iris-setosa", 1: "Iris-versicolor", 2: "Iris-virginica"}
        predicted_class = species_map.get(int(prediction[0]), 'unknown species')
        st.success(f"Predicted class: {predicted_class}")
