import streamlit as st
import config

st.set_page_config(page_title = config.PROJECT_NAME, layout = 'wide')

home = st.Page(
    page = "ViewPage/Home.py", 
    title = "Home", 
    icon = '🏠' 
)

dataExploration = st.Page(
    page = "ViewPage/Data_Exploration.py", 
    title = "Data Exploration", 
    icon = '📊' 
)

modelTraining = st.Page(
    page = "ViewPage/Model_Training.py", 
    title = "Model Training", 
    icon = '🤖' 
)

prediction = st.Page(
    page = "ViewPage/Prediction.py", 
    title = "Prediction", 
    icon = '🎯' 
)

conclusion = st.Page(
    page = "ViewPage/Conclusion.py", 
    title = "Conclusion", 
    icon = '🔍' 
)

st.logo('assets/logo.png', size = 'large')

pg = st.navigation({
    config.PROJECT_NAME:[home, dataExploration, modelTraining, prediction, conclusion]
})

pg.run()