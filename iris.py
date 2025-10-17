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
        if predicted_class == "Iris-setosa":
            st.image("https://thumbs.dreamstime.com/b/closeup-single-iris-setosa-flower-pretty-mauve-garden-228835113.jpg", caption="Iris-setosa", use_container_width=True)
        elif predicted_class == "Iris-versicolor":
            st.image("https://tse2.mm.bing.net/th/id/OIP.Slm0GQWYZWy5rghhQlF2aAHaHa?cb=12ucfimg=1&rs=1&pid=ImgDetMain&o=7&rm=3", caption="Iris-versicolor", use_container_width=True)
        elif predicted_class == "Iris-virginica":
            st.image("https://thvnext.bing.com/th/id/OIP.fT4cZGpZAKUxKFHbfHY_DQHaFh?w=253&h=188&c=7&r=0&o=7&cb=12&dpr=1.3&pid=1.7&rm=3&ucfimg=1", caption="Iris-virginica", use_container_width=True)
        else:
            st.warning("No image available for this prediction.")
