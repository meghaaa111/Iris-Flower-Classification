import streamlit as st
import pandas as pd
import joblib
from sklearn.tree import DecisionTreeClassifier

# Load the saved model
model = joblib.load('iris_model.pkl')

# App title and description
st.title("🌸 Iris Flower Classification App")
st.write("Predict the species of an Iris flower based on its measurements.")

# Sidebar inputs
st.sidebar.header("Enter Flower Measurements:")
sepal_length = st.sidebar.slider("Sepal Length (cm)", 4.0, 8.0, 5.1)
sepal_width = st.sidebar.slider("Sepal Width (cm)", 2.0, 4.5, 3.5)
petal_length = st.sidebar.slider("Petal Length (cm)", 1.0, 7.0, 1.4)
petal_width = st.sidebar.slider("Petal Width (cm)", 0.1, 2.5, 0.2)

# Predict button
if st.sidebar.button("Predict"):
    input_data = pd.DataFrame([[sepal_length, sepal_width, petal_length, petal_width]],
                              columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])
    
    prediction = model.predict(input_data)
    st.success(f"The predicted Iris species is: **{prediction[0]}**")
