import streamlit as st

# Page Title
st.title("Conclusion Page")

# Introduction to CRISP-ML(Q) Framework
st.header("CRISP-ML(Q) Methodology")
st.write("""
This project follows the **Cross-Industry Standard Process for Machine Learning with Quality Assurance (CRISP-ML(Q))** framework.  
It consists of six phases:
1. **Business and Data Understanding**
2. **Data Preparation**
3. **Model Building**
4. **Evaluation**
5. **Model Deployment**
6. **Maintenance and Monitoring**
""")

# Business Understanding
st.header("1. Business and Data Understanding")

st.subheader("Problem Statement")
st.write("""
A glass manufacturing company designs new glass materials using different earth elements based on customer requirements.  
Manual classification of glass types is time-consuming and inefficient.  
This project aims to automate the classification process using **K-Nearest Neighbors (KNN)**.
""")

st.subheader("Business Objectives")
st.write("- Maximize the speed and efficiency of the classification process.")

st.subheader("Business Constraints")
st.write("- Minimize manual classification efforts.")
st.write("- Ensure high customer satisfaction by delivering **accurate predictions**.")

# Data Understanding
st.header("2. Data Understanding")
st.write("""
The dataset consists of **chemical composition** features used to classify different types of glass.
""")

st.markdown("""
- **RI (Refractive Index):** Measures how light bends in glass.  
- **Na (Sodium):** Lowers melting point (from soda ash).  
- **Mg (Magnesium):** Increases durability and resistance.  
- **Al (Aluminum):** Improves chemical resistance.  
- **Si (Silicon):** Forms the glass structure (from silica).  
- **K (Potassium):** Enhances strength and clarity.  
- **Ca (Calcium):** Prevents glass from dissolving in water.  
- **Ba (Barium):** Increases refractive index and brilliance.  
- **Fe (Iron):** Controls color and UV absorption.  
""")

# Data Preparation
st.header("3. Data Preparation")
st.write("**Feature Engineering and Preprocessing Steps:**")

st.subheader("Feature Transformation")
st.write("- **Reciprocal Transformation:** Applied to **Calcium (Ca)**.")
st.write("- **Yeo-Johnson Transformation:** Applied to **Magnesium (Mg)**.")

st.subheader("Feature Scaling")
st.write("- Used **StandardScaler** to standardize features for consistent scaling.")

st.subheader("Handling Imbalanced Data")
st.write("- The target variable was **imbalanced**, so **SMOTE (Synthetic Minority Over-sampling Technique)** was used to balance the dataset.")

# Model Building
st.header("4. Model Building")
st.write("""
The model was developed using the **K-Nearest Neighbors (KNN) algorithm** with hyperparameter tuning.
- Used **GridSearchCV** to test `n_neighbors` values from **3 to 50**.
- The optimal value found was **n_neighbors = 3**.
""")

# Model Evaluation
st.header("5. Model Evaluation")
st.write("""
The model was evaluated using training and testing data:
- **Training Accuracy:** 93.5%
- **Testing Accuracy:** 89.5%
""")

# Model Deployment
st.header("6. Model Deployment")
st.write("""
The trained model is deployed using **Streamlit**, allowing users to interact with the model through a web-based interface.
""")

# Maintenance and Monitoring
st.header("7. Maintenance and Monitoring")
st.write("""
For continuous model updates and version control:
- **GitHub** is used to maintain and monitor the project repository.
""")

# Final Message
st.success("This project successfully automates glass type classification, improving accuracy, efficiency, and business productivity.")



