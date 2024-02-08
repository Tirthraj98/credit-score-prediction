import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('credit_score_prediction_model.joblib')



# Define function to make predictions
def predict_credit_score(data):
    predictions = model.predict(data)
    return predictions

# Define Streamlit app
def main():
    st.title('Credit Score Prediction Demo')
    st.write('Enter the details below to predict the credit score:')

    # Create input fields for user input
    age = st.number_input('Age', min_value=0, max_value=150, value=30)
    marital_status = st.selectbox('Marital Status', ['Single', 'Married', 'Divorced'])
    education_level = st.selectbox('Education Level', ['High School', 'Bachelor', 'Master', 'PhD'])
    dependents_count = st.number_input('Dependents Count', min_value=0)
    livestock_presence = st.checkbox('Livestock Presence')
    personal_vehicle_presence = st.checkbox('Personal Vehicle Presence')
    owns_house = st.checkbox('Owns House')
    owns_farm = st.checkbox('Owns Farm')
    farm_size_acres = st.number_input('Farm Size (Acres)', min_value=0.0)
    irrigation_presence = st.checkbox('Irrigation Presence')
    farming_technique = st.selectbox('Farming Technique', ['Traditional', 'Modern'])
    farming_tool = st.text_input('Farming Tool')
    yield_2_years_ago_tons = st.number_input('Yield 2 Years Ago (Tons)', min_value=0.0)
    investment_2_years_ago = st.number_input('Investment 2 Years Ago', min_value=0)
    profit_2_years_ago = st.number_input('Profit 2 Years Ago', min_value=0)
    yield_1_year_ago_tons = st.number_input('Yield 1 Year Ago (Tons)', min_value=0.0)
    investment_1_year_ago = st.number_input('Investment 1 Year Ago', min_value=0)
    profit_1_year_ago = st.number_input('Profit 1 Year Ago', min_value=0)
    market_trend = st.selectbox('Market Trend', ['Up', 'Down', 'Stable'])
    crop_name = st.text_input('Crop Name')

    # Create a button to trigger prediction
    if st.button('Predict'):
        # Prepare input data as a DataFrame
        input_data = pd.DataFrame({
            'Age': [age],
            'Marital_Status': [marital_status],
            'Education_Level': [education_level],
            'Dependents_Count': [dependents_count],
            'Livestock_Presence': [livestock_presence],
            'Personal_Vehicle_Presence': [personal_vehicle_presence],
            'Owns_House': [owns_house],
            'Owns_Farm': [owns_farm],
            'Farm_Size_Acres': [farm_size_acres],
            'Irrigation_Presence': [irrigation_presence],
            'Farming_Technique': [farming_technique],
            'Farming_Tool': [farming_tool],
            'Yield_2Years_Ago_Tons': [yield_2_years_ago_tons],
            'Investment_2Years_Ago': [investment_2_years_ago],
            'Profit_2Years_Ago': [profit_2_years_ago],
            'Yield_1Year_Ago_Tons': [yield_1_year_ago_tons],
            'Investment_1Year_Ago': [investment_1_year_ago],
            'Profit_1Year_Ago': [profit_1_year_ago],
            'Market_Trend': [market_trend],
            'Crop_Name': [crop_name],
        })
        # Make prediction
        prediction = predict_credit_score(input_data)
        # Display prediction
        st.write('Predicted Credit Score:', prediction[0])

if __name__ == '__main__':
    main()
