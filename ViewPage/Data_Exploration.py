import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Data Exploration - CrystalKNN")

# File uploader
uploaded_file = 'data/glass.csv'

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # Show first 5 rows
    st.subheader("Dataset Head (First 5 Rows)")
    st.write(df.head())
    
    # Show dataset description
    st.subheader("Dataset Description")
    st.write(df.describe())
    
    # Select a categorical column for bar chart
    st.subheader("Bar Chart Visualization - Target Values")
    target = 'Type'
    
    if target in df.columns:
        value_counts = df[target].value_counts().reset_index()
        value_counts.columns = ["Category", "Count"]
        fig = px.bar(
            value_counts,
            x="Category",
            y="Count",
            color="Category",
            text="Count",
            title=f"Bar Chart of {target}"
        )
        fig.update_traces(textposition='outside')
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.write("Target column not found in dataset.")
