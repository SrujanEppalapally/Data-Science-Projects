#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("dt.pkl","rb")
knn=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(age,gender,polyuria,polydipsia,sudden_weight_loss,weakness,Polyphagia,genital_thrush,visual_blurring,itching,Irritability,delayed_healing,partial_paresis,muscle_stiffness,Alopecia,Obesity):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
   
    prediction=knn.predict([[age,gender,polyuria,polydipsia,sudden_weight_loss,weakness,Polyphagia,genital_thrush,visual_blurring,itching,Irritability,delayed_healing,partial_paresis,muscle_stiffness,Alopecia,Obesity]])
    if prediction==1:
        return ' positive'
    else:
        return ' negative'



def main():
    st.title("Diabetes prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">DIABETES PREDICTION </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    age = st.text_input("age","Please enter your AGE here")
    gender = st.text_input("gender","PLEASE ENTER 1 IF YOU ARE MALE ELSE 0")
    polyuria = st.text_input("polyuria","PLEASE ENTER 1 IF YOU HAVE PLOYURIA ELSE 0")
    polydipsia = st.text_input("polydipsia","Type Here")
    sudden_weight_loss = st.text_input("sudden weight loss","Type Here")
    weakness = st.text_input("weakness","Type Here")
    Polyphagia = st.text_input("Polyphagia","Type Here")
    genital_thrush = st.text_input("Genital thrush","Type Here")
    visual_blurring = st.text_input("visual blurring","Type Here")
    itching = st.text_input("Itching","Type Here")
    Irritability = st.text_input("Irritability","Type Here")
    delayed_healing = st.text_input("delayed healing","Type Here")
    partial_paresis = st.text_input("partial paresis","Type Here")
    muscle_stiffness = st.text_input("muscle stiffness","Type Here")
    Alopecia = st.text_input("Alopecia","Type Here")
    Obesity = st.text_input("Obesity","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(age,gender,polyuria,polydipsia,sudden_weight_loss,weakness,Polyphagia,genital_thrush,visual_blurring,itching,Irritability,delayed_healing,partial_paresis,muscle_stiffness,Alopecia,Obesity)
    st.success('The output is{}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()

