import streamlit as st
import pandas as pd

st.set_page_config(page_title="DataFetcher", layout="wide")
st.title("📊 DataFetcher - Condition Row Fetcher")

uploaded_file = st.file_uploader("Upload CSV or Excel file", type=["csv", "xlsx"])
if uploaded_file:
    try:
        # Load file into DataFrame
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.success("File loaded successfully!")
        st.write("### Preview of Data", df.head())

        # Column selector
        selected_column = st.selectbox("Select attribute column to filter by", df.columns)
        if selected_column:
            unique_values = df[selected_column].dropna().unique().tolist()
            selected_value = st.selectbox(f"Select value from '{selected_column}'", unique_values)
            if selected_value is not None:
                filtered_df = df[df[selected_column] == selected_value]
                st.write(f"### Rows where `{selected_column}` = `{selected_value}`")
                st.dataframe(filtered_df)
                st.download_button("Download Filtered Data as CSV", filtered_df.to_csv(index=False), file_name="filtered_data.csv", mime="text/csv")

    except Exception as e:
        st.error(f"Error: {str(e)}")
