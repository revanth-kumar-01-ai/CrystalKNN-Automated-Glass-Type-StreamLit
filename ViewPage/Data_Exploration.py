import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Data Exploration - CrystalKNN")

# Show first 5 rows
st.subheader("Dataset Head (First 5 Rows)")
st.image('./assets/head5.png')

# Show dataset description
st.subheader("Dataset Description")
st.image('./assets/description.png')

# Select a categorical column for bar chart
st.subheader("Bar Chart Visualization - Target Values")

value_counts = pd.DataFrame({'Category': ["2", "1", "7", "3", "5", "8"], 'Count': [76, 70, 29, 17, 13, 9]})

fig = px.bar(
        value_counts,
        x="Category",
        y="Count",
        color="Category",
        text="Count",
        title=f"Bar Chart of Type"
    )
fig.update_traces(textposition='outside')
st.plotly_chart(fig, use_container_width=True)