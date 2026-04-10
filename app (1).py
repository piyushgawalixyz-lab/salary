import streamlit as st
import pickle
import numpy as np

# Load the saved model
with open('best_salary_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("💸 Salary Prediction App")
st.write("Enter the details below to estimate the salary.")

# Input fields based on your features: Age, Gender, Education Level, Job Title, Years of Experience
age = st.number_input("Age", min_value=18, max_value=70, value=30)
gender = st.selectbox("Gender", options=[0, 1], format_func=lambda x: "Male" if x == 1 else "Female")
edu = st.selectbox("Education Level (Encoded)", options=[0, 1, 2, 3, 4, 5]) 
job = st.number_input("Job Title (Encoded ID)", min_value=0, max_value=200, value=177)
exp = st.number_input("Years of Experience", min_value=0.0, max_value=50.0, value=5.0)

if st.button("Predict Salary"):
    features = np.array([[age, gender, edu, job, exp]])
    prediction = model.predict(features)
    st.success(f"Estimated Salary: ${prediction[0]:,.2f}")
