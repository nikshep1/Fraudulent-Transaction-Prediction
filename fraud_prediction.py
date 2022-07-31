# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 18:57:06 2022

@author: rakes
"""

import numpy as np
import pickle 
import streamlit as st

loaded_model = pickle.load(open('C:/Users/rakes/NEW DEPLOYMENT/trained_model.sav', 'rb'))


def fraud_prediction(input_data2):

    input_data_as_numpy_array = np.asarray(input_data2)

    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    if (prediction[0] == 0):
        return'Not Fraud'
    else:
        return'Fraud'
        
        
        
        
def main():
    
    st.title('Fraudulent Transaction Prediction Web APP')
        
    amount = st.number_input('Amount')
    oldbalanceOrg = st.number_input('oldbalanceOrg')
    newbalanceOrig = st.number_input('newbalanceOrig')
    oldbalanceDest = st.number_input('oldbalanceDest')
    newbalanceDest = st.number_input('newbalanceDest')
    Type = st.number_input('Type')
    days = st.number_input('days')
    
    predict = ''
    
    if st.button('Fraud Prediction'):
        predict = fraud_prediction([amount, oldbalanceOrg, newbalanceOrig, oldbalanceDest, newbalanceDest, Type, days])
        
        
    st.success(predict)
    
    
    
if __name__ == '__main__':
    main()
    




    