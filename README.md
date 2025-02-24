# CrystalKNN - Automated Glass Type Classification

## Overview
This project automates the classification of glass types using machine learning, specifically the **K-Nearest Neighbors (KNN)** algorithm. The classification process is optimized to replace manual efforts, improving efficiency and accuracy for a **glass manufacturing company**.

## Dataset
- **Features & Target Variable**:
  - The dataset contains **9 chemical composition features** that determine glass type.
  - The **target variable** classifies glass into **6 types** based on their usage and composition.
- **Dataset Size**:
  - **Rows**: 214
  - **Columns**: 10 (including the target variable)
- **Preprocessing Steps**:
  - **Feature Transformation**:
    - **Reciprocal Transformation** applied to **Calcium (Ca)**.
    - **Yeo-Johnson Transformation** applied to **Magnesium (Mg)**.
  - **Feature Scaling**: Standardized using **StandardScaler**.
  - **Handling Imbalanced Data**: **SMOTE (Synthetic Minority Over-sampling Technique)** used for class balancing.

## Technologies Used
- **Programming Language**: Python
- **Libraries**:
  - Data Processing: `pandas`, `NumPy`
  - Machine Learning: `scikit-learn`, `imbalanced-learn`
  - Model Deployment: `Streamlit`
  - Hyperparameter Tuning: `GridSearchCV`
- **Tools**:
  - **Jupyter Notebook** for model development
  - **Streamlit** for deploying the web application
  - **GitHub** for version control and monitoring

## Data Preprocessing
- **Handling Missing Values**:
  - Checked for missing values (none found in this dataset).
- **Encoding Categorical Variables**:
  - No categorical variables in the dataset.
- **Feature Engineering & Scaling**:
  - **Transformation**: Addressed skewness in **Ca and Mg** using appropriate transformations.
  - **Scaling**: Applied **StandardScaler** to ensure uniform feature distribution.

## Model Training
- **Algorithm Used**: **K-Nearest Neighbors (KNN)**
- **Hyperparameter Tuning**:
  - Used **GridSearchCV** to optimize `n_neighbors` from **3 to 50**.
  - Best parameter: `n_neighbors = 3`.
- **Evaluation Metrics**:
  - **Training Accuracy**: 93.5%
  - **Test Accuracy**: 89.5%

## Model Deployment
- **Deployment Framework**: **Streamlit**
- **Usage Instructions**:
  1. Clone the repository:
     ```bash
     git clone https://github.com/revanth-kumar-01-ai/CrystalKNN-Automated-Glass-Type-StreamLit.git
     cd CrystalKNN
     ```
  2. Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```
  3. Run the Streamlit app:
     ```bash
     streamlit run app.py
     ```
  4. The web interface will open in the browser, allowing users to input chemical compositions and classify the glass type.

## Maintenance & Monitoring
- **Version Control**: The project is maintained using **GitHub** for continuous monitoring and updates.

## Conclusion
This project successfully **automates glass type classification**, improving accuracy and efficiency in the **manufacturing industry**. By implementing **KNN with optimized hyperparameters**, the model achieves **high accuracy** while maintaining **scalability and ease of deployment**.
