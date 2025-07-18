import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title("CSV Dataset Viewer")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# Check if file is uploaded
if uploaded_file is not None:
    # Read CSV file
    df = pd.read_csv(uploaded_file)
    # chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    df = df.dropna(subset=['release_year'])

    df['range'] = pd.cut(df['release_year'], bins=np.arange(2006, 2017, 1))
    counts = df['range'].value_counts().sort_index()
    # Convert to DataFrame for Plotly
    chart_df = counts.reset_index()
    chart_df.columns = ['Range', 'Count']
    chart_df['Range'] = chart_df['Range'].astype(str)  # Convert to string for labels

    # Create colored bar chart
    fig = px.bar(chart_df, x='Range', y='Count', color='Range', title='Rating Ranges')

    # Show in Streamlit
    st.plotly_chart(fig)

    # counts.index = counts.index.astype(str)

    # st.bar_chart(counts)


    # Show the data
    st.subheader("Dataset Preview")
    st.dataframe(df)

    # Optional: show basic info
    st.subheader("Summary Statistics")
    st.write(df.head())
else:
    st.info("Please upload a CSV file to begin.")