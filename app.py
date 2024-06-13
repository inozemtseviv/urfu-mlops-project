import streamlit as st
import joblib
import numpy as np
import pandas as pd


@st.cache_resource
def load_model():
    return joblib.load('./models/model.pkl')


st.title('Определение качества красного вина по его параметрам')

with st.sidebar:
    st.title('Параметры')
    fixed_acidity = st.slider(label='fixed acidity', min_value=4.0, max_value=16.0, value=8.3, step=0.1)
    volatile_acidity = st.slider(label='volatile acidity', min_value=0.1, max_value=1.6, value=0.5, step=0.1)
    citric_acid = st.slider(label='citric acid', min_value=0.0, max_value=1.0, value=0.3, step=0.1)
    residual_sugar = st.slider(label='residual sugar', min_value=0.9, max_value=16.0, value=2.5, step=0.1)
    chlorides = st.slider(label='chlorides', min_value=0.1, max_value=0.7, value=0.1, step=0.1)
    free_sulfur_dioxide = st.slider(label='free sulfur dioxide', min_value=1.0, max_value=72.0, value=16.0, step=1.0)
    total_sulfur_dioxide = st.slider(label='total sulfur dioxide', min_value=6.0, max_value=289.0, value=47.0, step=1.0)
    density = st.slider(label='density', min_value=0.98, max_value=1.9, value=0.99, step=0.01)
    pH = st.slider(label='pH', min_value=2.6, max_value=4.01, value=3.3, step=0.01)
    sulphates = st.slider(label='sulphates', min_value=0.33, max_value=2.0, value=0.65, step=0.01)
    alcohol = st.slider(label='alcohol', min_value=8.4, max_value=14.9, value=10.4, step=0.1)

model = load_model()

data = np.array([
    fixed_acidity,
    volatile_acidity,
    citric_acid,
    residual_sugar,
    chlorides,
    free_sulfur_dioxide,
    total_sulfur_dioxide,
    density,
    pH,
    sulphates,
    alcohol,
])

input_data = pd.DataFrame(
    data=[data],
    columns=[
        'fixed acidity',
        'volatile acidity',
        'citric acid',
        'residual sugar',
        'chlorides',
        'free sulfur dioxide',
        'total sulfur dioxide',
        'density',
        'pH',
        'sulphates',
        'alcohol',
    ]
)

prediction = model.predict(input_data)

st.markdown(
    f"<h2 style='font-size:80px; text-align:center;'>Качество: {prediction[0]} из 8</h2>", 
    unsafe_allow_html=True
)
