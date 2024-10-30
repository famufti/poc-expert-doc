import streamlit as st
import requests
import time

# Set the page title
st.set_page_config(page_title="Patient's Data Analyzer")

# Page title
st.title("Patient's Data Analyzer")

# Create form for file and text inputs
with st.form("patient_form"):
    file = st.file_uploader("Select a file", type=["jpg", "png", "pdf"])
    text_field1 = st.text_input("Enter patient ID")
    text_field2 = st.text_input("Enter doctor's name")
    text_field3 = st.text_input("Enter additional notes")
    
    submit_button = st.form_submit_button("Submit")

# Handle form submission
if submit_button:
    if file and text_field1 and text_field2 and text_field3:
        with st.spinner("Analyzing data..."):
            # Define the API endpoint and prepare data for the request
            endpoint_url = "https://example.com/api/upload"  # Replace with your API endpoint
            files = {"file": file.getvalue()}
            data = {
                "patient_id": text_field1,
                "doctor_name": text_field2,
                "notes": text_field3
            }

            # Make the curl call (POST request in this case)
            try:
                response = requests.post(endpoint_url, files=files, data=data)
                response.raise_for_status()  # Check for request errors
                result = response.json()  # Parse JSON response
                st.success("Data analyzed successfully!")
                st.json(result)  # Display response data
            except requests.exceptions.RequestException as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please fill in all fields and upload a file.")
