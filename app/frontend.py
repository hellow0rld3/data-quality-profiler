import streamlit as st
import requests

st.title("🧹 DATA QUALITY PROFILER")

uploaded_file = st.file_uploader("Upload file", type=["csv"])

if uploaded_file is not None:
    files = {"file": (uploaded_file.name, uploaded_file.getvalue(), "text/csv")}
    response = requests.post("http://127.0.0.1:8000/upload", files=files)
    dane = response.json()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(label="Data Quality Score", value=f"{dane['ocena_pliku']}")

    with col2:
        st.metric(label="Missing Values", value=f"{dane['brakujace_wartosci']}")
    
    with col3:
        st.metric(label="Duplicated Rows", value=f"{dane['zduplikowane_wiersze']}")

    st.write("---") 

    if st.button("Clean Data"):
        with st.spinner("Cleaning and hunting anomalies..."):
            response2 = requests.post("http://127.0.0.1:8000/clean", files=files)
            cleaned_data = response2.content

            st.download_button(
                label="Download Cleaned CSV", 
                data=cleaned_data,
                file_name="cleaned_dataset.csv", 
                mime="text/csv"
            )