import streamlit as st
import pandas as pd
from PIL import Image
import pickle
st.title("Carbon Emission Predictor")

Engine_size= st.text_input("Enter engine size(in Liters from 0 to 10): ")

cylinders = st.text_input("Enter the number of cylinders", "Type Here ...")

transmission = st.text_input("Enter the type of transmission (from 0-4), Eg:- 0-A,1-AM, 2-AS, 3-AV, 4-M")

gears= st.number_input("Enter engine size(0 to 10): ")

fuel=st.selectbox("Fuel Type: ",[0,1,2,3])

fuel_cc=st.text_input("Enter the fuel consumption city in litres")

fuel_ch=st.text_input("Enter the fuel consumption highway in litres")

fuel_comb=st.text_input("Enter the fuel consumption combination in litres")

fuel_mpg=st.text_input("Enter the fuel consumption combination in miles per gram")

model=st.selectbox("Select the model to predict: ",['Decision Tree','Artificial Neural Network', 'K Neighbors'])

diction={'Decision Tree':'decisionTree.pkl','Artificial Neural Network':'ann.pkl','K Neighbors':'knn.pkl'}

submit=st.button("Submit")
if (submit):
    pkl_file=diction[model]
    with open('pkl_file.pkl','rb') as file:
        modex=pickle.load(file)
    result = modex.predict(float(Engine_size),
                           int(cylinders),
                           int(transmission),
                           int(gears),
                           int(fuel),
                           float(fuel_cc),
                           float(fuel_ch),
                           float(fuel_comb),
                           float(fuel_mpg))
    
    st.write(result)

