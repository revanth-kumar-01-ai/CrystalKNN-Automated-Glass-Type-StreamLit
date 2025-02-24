import streamlit as st
import pandas as pd
from utils.preprocessing import DataPreProcessing
from utils.model_utils import Model


st.title("CrystalKNN - Glass Type Prediction")

col1, col2, col3 = st.columns(3)

with col1:
    Refractive = st.number_input("Refractive (RI)", min_value=0.0, step=0.1, value=1.52101)
    Sodium = st.number_input("Sodium (Na)", min_value=0.0, step=0.1, value = 13.64) 
    Magnesium = st.number_input("Magnesium (Mg)", min_value=0.0, step=0.1, value = 4.49)

with col2:
    Aluminum = st.number_input("Aluminum (Al)", min_value=0.0, step=0.1, value = 1.1)
    Silicon = st.number_input("Silicon (Si)", min_value=0.0, step=0.1, value = 71.78)
    Potassium = st.number_input("Potassium (K)", min_value=0.0, step=0.1, value = 0.06)

with col3:
    Calcium = st.number_input("Calcium (Ca)", min_value=0.0, step=0.1, value = 8.75) 
    Barium = st.number_input("Barium (Ba)", min_value=0.0, step=0.1,value = 0.0)
    Iron = st.number_input("Iron (Fe)", min_value=0.0, step=0.1,value = 0.0)

# Submit button
if st.button("Predict"):
    df = pd.DataFrame([[Refractive, Sodium, Magnesium, Aluminum, Silicon, Potassium, Calcium, Barium, Iron]], 
                          columns=["RI", "Na", "Mg", "Al", "Si", "K", "Ca", "Ba", "Fe"])
    
    st.write("### User Input Data")
    st.dataframe(df)
 
    data = DataPreProcessing(df)

    print(data)
   
    predict = Model(data)
    st.success(f"### The predicted glass type is: **{predict}**")