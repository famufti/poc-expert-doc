import streamlit as st
import requests
import time
import json

# Set the page title
st.set_page_config(page_title="Patient's Data Analyzer")

# Page title
st.title("Patient's Data Analyzer")

# Create form for file and text inputs
with st.form("patient_form"):
    file = st.file_uploader("Select a file", type=["jpg", "png", "pdf"])
    text_patient_id = st.text_input("Enter Patient ID")
    text_report_type = st.text_input("Enter Record Type")
    text_report_id = st.text_input("Enter Report ID")

    submit_button = st.form_submit_button("Submit")

# Handle form submission
if submit_button:
    if text_patient_id and text_report_type and text_report_id:
        print("hello")

        # Define the API endpoint and prepare data for the request
        # endpoint_url = "https://gyjbea39k8.execute-api.us-west-2.amazonaws.com/dev/v1"
        # # files = {"file": file.getvalue()}
        # data = {
        #     "patient_id": text_patient_id,
        #     "report_type": text_report_type,
        #     "report_id": text_report_id
        # }

        endpoint_url = "https://gyjbea39k8.execute-api.us-west-2.amazonaws.com/dev/v1"

        payload = json.dumps({
            "patient_id": text_patient_id,
            "report_type": text_report_type,
            "report_id": text_report_id
        })
        headers = {
            'Content-Type': 'application/json'
        }

        # Make the curl call (POST request in this case)
        try:
            # # response = requests.post(endpoint_url, files=files, data=data)
            # response = requests.post(endpoint_url, data=data)
            # response.raise_for_status()  # Check for request errors
            # result = response.json()  # Parse JSON response
            # print(result)
            #
            # st.success("Data analyzed successfully!")
            # st.json(result)  # Display response data

            response = requests.request("POST", endpoint_url, headers=headers, data=payload)
            # st.text_input(response.text)

            result = json.loads(response.text)  # Parse JSON response
            # st.text_input(result)
            st.text_input(result["body"]["url"])

        except requests.exceptions.RequestException as e:
            st.error(f"An error occurred: {e}")

    # if file:
    #     with st.spinner("Analyzing data..."):
    # else:
    #     st.warning("Please fill in all fields and upload a file.")
