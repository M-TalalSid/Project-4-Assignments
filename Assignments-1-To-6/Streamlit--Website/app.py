import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page Configuration
st.set_page_config(page_title="My New App", layout="wide")

# Custom Styling
st.markdown(
    """
    <style>
        .main {
            background-color: #f4f4f4;
        }
        h1 {
            color: #0066cc;
            text-align: center;
        }
        .stButton>button {
            background-color: #0066cc;
            color: white;
            font-size: 16px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# App Title and Introduction
st.title("My New App")
st.write("Welcome to My New App – an interactive data dashboard built with Streamlit!")

# Sidebar for File Upload
st.sidebar.header("Upload Your CSV File")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)
    
    # Show a preview of the first 10 rows of data
    st.subheader("📌 Data Preview")
    st.dataframe(df.head(10))
    
    # Sidebar: Data Filtering Options
    st.sidebar.header("Filter Data")
    columns = df.columns.tolist()
    selected_filter_column = st.sidebar.selectbox("Select column to filter by", columns)
    
    # Check if the selected column is likely categorical or numeric
    if df[selected_filter_column].dtype == 'object' or df[selected_filter_column].nunique() < 20:
        unique_values = df[selected_filter_column].unique()
        selected_filter_value = st.sidebar.selectbox("Select value", unique_values)
        filtered_df = df[df[selected_filter_column] == selected_filter_value]
    else:
        # For numeric columns, allow the user to select a range
        min_value = float(df[selected_filter_column].min())
        max_value = float(df[selected_filter_column].max())
        selected_range = st.sidebar.slider("Select range", min_value, max_value, (min_value, max_value))
        filtered_df = df[(df[selected_filter_column] >= selected_range[0]) & (df[selected_filter_column] <= selected_range[1])]
    
    st.sidebar.write("Filtered Data Preview:")
    st.sidebar.dataframe(filtered_df.head(10))
    
    # Display Data Summary
    st.subheader("📈 Data Summary")
    st.write(df.describe(include='all'))
    
    # Data Visualization Options
    st.subheader("📊 Data Visualization")
    viz_type = st.selectbox("Choose Chart Type", ["Line Chart", "Bar Chart", "Scatter Plot", "Histogram"])
    x_column = st.selectbox("Select x-axis column", columns, key="x_viz")
    y_column = st.selectbox("Select y-axis column", columns, key="y_viz")
    
    if st.button("Generate Chart"):
        if viz_type == "Line Chart":
            if x_column == y_column:
                st.warning("⚠️ Please select different columns for the x-axis and y-axis for a line chart.")
            else:
                st.line_chart(filtered_df.set_index(x_column)[y_column])
        elif viz_type == "Bar Chart":
            fig, ax = plt.subplots()
            # Group by x_column and calculate the mean of y_column values
            filtered_df.groupby(x_column)[y_column].mean().plot(kind='bar', ax=ax, color="#0066cc")
            ax.set_ylabel(y_column)
            st.pyplot(fig)
        elif viz_type == "Scatter Plot":
            fig, ax = plt.subplots()
            ax.scatter(filtered_df[x_column], filtered_df[y_column], color="#0066cc")
            ax.set_xlabel(x_column)
            ax.set_ylabel(y_column)
            st.pyplot(fig)
        elif viz_type == "Histogram":
            fig, ax = plt.subplots()
            ax.hist(filtered_df[x_column], bins=20, color="#0066cc")
            ax.set_xlabel(x_column)
            ax.set_ylabel("Frequency")
            st.pyplot(fig)
else:
    st.warning("📂 Please upload a CSV file to get started!")