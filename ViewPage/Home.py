import streamlit as st 

st.title("Assignment: CrystalKNN - Automated Glass Type Classification")

st.subheader('Problem Statement')
st.write('A glass manufacturing plant uses different earth elements to design new glass materials based on customer requirements. They would like to automate the classification process, as manually classifying glass types is tedious and time-consuming. Your task is to help the company achieve its objective by accurately classifying glass types based on their features using the KNN algorithm.')

st.header("Business Objectives")
st.write('Maximize the speed of the classification process.')

st.header("Business Constraints")
st.write('Minimize manual classification efforts.')
st.write('Ensure high customer satisfaction by delivering accurate results.')

st.header('Success Criteria')

st.write('**Business Success Criteria**')
st.write('Increase production efficiency.')

st.write('**Machine Learning Success Criteria**')
st.write('Achieve an accuracy of at least 80% in glass type classification.')

st.write('**Economic Success Criteria**')
st.write('Increase profitability by at least 25%.')

st.write("""

#### Dataset description

- RI	**Refractive Index**	-> Measures how light bends in glass.
- Na	**Sodium (Na)**	-> Lowers melting point (from soda ash).
- Mg	**Magnesium (Mg)**	-> Increases durability and resistance.
- Al	**Aluminum (Al)**	-> Improves chemical resistance.
- Si	**Silicon (Si)**	-> Forms the glass structure (from silica).
- K	    **Potassium (K)**	-> Enhances strength and clarity.
- Ca	**Calcium (Ca)**	-> Prevents glass from dissolving in water.
- Ba	**Barium (Ba)**	-> Increases refractive index and brilliance.
- Fe	**Iron (Fe)**	-> Controls color and UV absorption.

""")