# Importing needed libraries
import streamlit as st
import joblib
import math
import pandas as pd


# Function to predict yearly rent
def prediction():
    # Collecting The user input in a key and converting it to a dataframe
    predictdict = {'ACCOMODATION TYPE': ACCOMODATIONTYPEDROP, 'ROOM SIZE': ROOMSIZEDROP, 'BUILDING AGE': BUILDINGAGEDROP,  'ELECTRICITY RELIABILITY': ELECTRICITYRELIABILITYDROP, 'TOILET LOCATION':TOILETLOCATIONDROP, 'SECURITY GUARD?':SECURITYGUARDDROP, 'FENCE?': FENCEDROP, 'LOCATION OF WATER SOURCE': LOCATIONOFWATERSOURCEDROP}
    predictdata = pd.DataFrame.from_records([predictdict])
    
    # Loading the label encoder and the model
    ohe, feature_names = joblib.load('Encoder')
    model = joblib.load('best_lodge_prediction_model')
    
    # Predicting the rent, setting the ranges and writing it to my streamlit webpage
    predictdata = pd.DataFrame(ohe.transform(predictdata), columns=feature_names)
    rent = model.predict(predictdata)
    lower = math.ceil(rent[0] - 37000) 
    higher = math.ceil(rent[0] + 37000)
    st.write(f'The Yearly Rent of the lodge would be between \u20A6{format(math.ceil(lower/1000)*1000, ",d")} and \u20A6{format(math.ceil(higher/1000)*1000, ",d")}, but the exact prediction is \u20A6{format(math.ceil(math.ceil(rent[0])/1000)*1000, ",d")}')
    

# This is where i designed my streamlit webpage
st.title('LODGE YEARLY RENT PREDICTION ')
st.write('Select options from the drop down menu to predict the price of any kind of lodge')

ACCOMODATIONTYPEDROP = st.selectbox('What kind of accomodation do you want?', ['Single room', 'Self-con', 'Flat'])

ROOMSIZEDROP = st.selectbox('What size of room would you want?', ['Small', 'Medium', 'Large', 'Very Large', 'Very Small'])

BUILDINGAGEDROP = st.selectbox('Select how old you would want the lodge to be?', ['<5 years', '>20 years', '10-20 years'])

ELECTRICITYRELIABILITYDROP = st.selectbox('How reliable should the electricity at the lodge be?', ['Moderately reliable', 'Very reliable', 'Unreliable', 'No Light', 'Very unreliable'])

TOILETLOCATIONDROP = st.selectbox('Where would you like your toilet to be located?', ['En-suite', 'Shared', 'Outside'])

FENCEDROP = st.selectbox('Would you like your lodge to have a fence?', ['No', 'Yes'])

SECURITYGUARDDROP = st.selectbox('Would you like your lodge to have a security guard?', ['No', 'Yes', 'Sometimes'])

LOCATIONOFWATERSOURCEDROP = st.selectbox('how far will your primary source of water be located from your lodge?', ['5-15 min', 'Within compound', '>30 min', '15-30 min'])


if st.button('PREDICT YEARLY RENT!'):
    prediction()
    
