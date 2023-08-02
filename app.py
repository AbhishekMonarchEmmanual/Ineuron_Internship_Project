import streamlit as st 
from airline.entity.config import *
from airline.utils import *
from templates.input_webpage import *
import pandas as pd 
import os , sys
from airline.exception import airlineException

if __name__ == "__main__":
    try:
        webpage  = Prediction_input()                
        title_input_page = webpage.my_title_page()
        
        
        
        if st.checkbox("Lets Train and create model"):
                
                model = load_object('model.pkl')
                preprocessor  = load_object('preprocessor.pkl')
                df = pd.read_csv('airline.csv')
                df= feature_eng(df_path='airline.csv', col= ["Arrival_Time",'Date_of_Journey',"Duration", "Dep_Time","Route", "Additional_Info"])
                df = preprocessor.transform(df)
                y_pred = model.predict(df)
                st.write(y_pred)
                
                
                
    except Exception as e:
        raise airlineException(e,sys)
          