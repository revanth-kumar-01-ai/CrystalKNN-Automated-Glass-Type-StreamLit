import streamlit as st

st.title("Model Training Code - CrystalKNN")

# Description and code snippet for SMOTE
st.subheader("1. Handling Imbalanced Data with SMOTE")
st.write("SMOTE (Synthetic Minority Over-sampling Technique) is used to balance the dataset by generating synthetic samples for minority classes.")
st.code("""
from imblearn.over_sampling import SMOTE

# Apply SMOTE for balancing classes
smote = SMOTE(sampling_strategy='auto', random_state=42)
X_resampled, y_resampled = smote.fit_resample(independent, dependent)
""", language="python")

# Description and code snippet for train-test split
st.subheader("2. Splitting Data into Training and Testing Sets")
st.write("The dataset is split into 80% training and 20% testing using `train_test_split`. Stratification is applied to maintain class proportions.")
st.code("""
from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(
    X_resampled, y_resampled, test_size=0.2, random_state=42, stratify=y_resampled
)
""", language="python")

# Description and code snippet for KNN with GridSearchCV
st.subheader("3. Finding the Best KNN Model with GridSearchCV")
st.write("GridSearchCV is used to find the best hyperparameter (`n_neighbors`) for KNN by evaluating multiple values.")
st.code("""
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier

# Parameter grid
param_grid = {'n_neighbors': list(range(3, 50, 2))}

# KNN model with GridSearchCV
knn = KNeighborsClassifier()
grid = GridSearchCV(knn, param_grid, cv=5, scoring='accuracy')
grid.fit(X_train, Y_train)

# Best estimator
knn_best = grid.best_estimator_
""", language="python")

# Description and code snippet for saving the model
st.subheader("4. Saving the Trained Model")
st.write("The trained KNN model is saved using `pickle`, which allows us to reuse it later without retraining.")
st.code("""
import pickle

# Save model
with open('./models/glass_AI_model.pkl', 'wb') as model_file:
    pickle.dump(knn_best, model_file)
""", language="python")
