# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 18:46:17 2022

@author: rakes
"""
import numpy as np 
import pickle 

loaded_model = pickle.load(open('C:/Users/rakes/NEW DEPLOYMENT/trained_model.sav', 'rb'))

from sklearn.utils.validation import check_array as check_arrays
input_data = (339682.13, 339682.13, 0.0, 0.00, 339682.13, 2, 1)
input_data1 = np.array(input_data, dtype=float)
input_data2 = [float(i) for i in input_data]
input_data_as_numpy_array = np.asarray(input_data2)


input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
check_arrays(input_data_reshaped, dtype='object')
prediction = loaded_model.predict(input_data_reshaped)
print(prediction)
if (prediction[0] == 0):
    print('Not Fraud')
else:
    print('Fraud')