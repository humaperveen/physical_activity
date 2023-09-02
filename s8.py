#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import joblib

# Load the Decision Tree model using joblib
dt_model = joblib.load('decision_tree_model_new.joblib')

# App title and header
st.title('Activity Prediction App')
st.subheader('Enter the values of the features for prediction:')

# Activity name mapping
activity_mapping = {
    1: 'transient activities',
    2: 'lying',
    3: 'sitting',
    4: 'standing',
    5: 'ironing',
    6: 'vacuum cleaning',
    7: 'ascending stairs',
    8: 'descending stairs',
    9: 'walking',
    10: 'Nordic walking',
    11: 'cycling',
    12: 'running',
    13: 'rope jumping'
}

# Function to perform prediction
def predict_activity(data):
    prediction = dt_model.predict(data)
    return prediction[0]

# Create input fields for each feature
heart_rate = st.number_input('Heart Rate')
hand_temperature = st.number_input('Hand Temperature (°C)')
hand_accel_x = st.number_input('Hand Acceleration X ±16g')
hand_accel_y = st.number_input('Hand Acceleration Y ±16g')
hand_accel_z = st.number_input('Hand Acceleration Z ±16g')
hand_gyro_x = st.number_input('Hand Gyroscope X')
hand_gyro_y = st.number_input('Hand Gyroscope Y')
hand_gyro_z = st.number_input('Hand Gyroscope Z')
hand_magnet_x = st.number_input('Hand Magnetometer X')
hand_magnet_y = st.number_input('Hand Magnetometer Y')
hand_magnet_z = st.number_input('Hand Magnetometer Z')
chest_temperature = st.number_input('Chest Temperature (°C)')
chest_accel_x = st.number_input('Chest Acceleration X ±16g')
chest_accel_y = st.number_input('Chest Acceleration Y ±16g')
chest_accel_z = st.number_input('Chest Acceleration Z ±16g')
chest_gyro_x = st.number_input('Chest Gyroscope X')
chest_gyro_y = st.number_input('Chest Gyroscope Y')
chest_gyro_z = st.number_input('Chest Gyroscope Z')
chest_magnet_x = st.number_input('Chest Magnetometer X')
chest_magnet_y = st.number_input('Chest Magnetometer Y')
chest_magnet_z = st.number_input('Chest Magnetometer Z')
ankle_temperature = st.number_input('Ankle Temperature (°C)')
ankle_accel_x = st.number_input('Ankle Acceleration X ±16g')
ankle_accel_y = st.number_input('Ankle Acceleration Y ±16g')
ankle_accel_z = st.number_input('Ankle Acceleration Z ±16g')
ankle_gyro_x = st.number_input('Ankle Gyroscope X')
ankle_gyro_y = st.number_input('Ankle Gyroscope Y')
ankle_gyro_z = st.number_input('Ankle Gyroscope Z')
ankle_magnet_x = st.number_input('Ankle Magnetometer X')
ankle_magnet_y = st.number_input('Ankle Magnetometer Y')
ankle_magnet_z = st.number_input('Ankle Magnetometer Z')

# Predict button
if st.button('Predict'):
    # Create a DataFrame with the input data
    data = pd.DataFrame({
        'heart_rate': [heart_rate],
        'hand temperature (°C)': [hand_temperature],
        'hand acceleration X ±16g': [hand_accel_x],
        'hand acceleration Y ±16g': [hand_accel_y],
        'hand acceleration Z ±16g': [hand_accel_z],
        'hand gyroscope X': [hand_gyro_x],
        'hand gyroscope Y': [hand_gyro_y],
        'hand gyroscope Z': [hand_gyro_z],
        'hand magnetometer X': [hand_magnet_x],
        'hand magnetometer Y': [hand_magnet_y],
        'hand magnetometer Z': [hand_magnet_z],
        'chest temperature (°C)': [chest_temperature],
        'chest acceleration X ±16g': [chest_accel_x],
        'chest acceleration Y ±16g': [chest_accel_y],
        'chest acceleration Z ±16g': [chest_accel_z],
        'chest gyroscope X': [chest_gyro_x],
        'chest gyroscope Y': [chest_gyro_y],
        'chest gyroscope Z': [chest_gyro_z],
        'chest magnetometer X': [chest_magnet_x],
        'chest magnetometer Y': [chest_magnet_y],
        'chest magnetometer Z': [chest_magnet_z],
        'ankle temperature (°C)': [ankle_temperature],
        'ankle acceleration X ±16g': [ankle_accel_x],
        'ankle acceleration Y ±16g': [ankle_accel_y],
        'ankle acceleration Z ±16g': [ankle_accel_z],
        'ankle gyroscope X': [ankle_gyro_x],
        'ankle gyroscope Y': [ankle_gyro_y],
        'ankle gyroscope Z': [ankle_gyro_z],
        'ankle magnetometer X': [ankle_magnet_x],
        'ankle magnetometer Y': [ankle_magnet_y],
        'ankle magnetometer Z': [ankle_magnet_z]
    })

    # Perform prediction
    prediction_result = predict_activity(data)
    st.subheader('Predicted Activity:')
    st.write(activity_mapping[prediction_result])


# In[ ]:





# In[ ]:




