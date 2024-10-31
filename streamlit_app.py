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

    submit_button = st.form_submit_button("Submit")

# Handle form submission
if submit_button:

    if text_patient_id and text_report_type and file:

        file_name = file.name
        text_report_id = file_name

        # Created data for Curl call
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
            response = requests.request("POST", endpoint_url, headers=headers, data=payload)
            result = json.loads(response.text)  # Parse JSON response
            body = json.loads(result["body"])
            presigned_url = body["url"]

            st.write(presigned_url)
            st.write("-----------------------------------------------------------")

            # upload image file to s3 using pre-signed URLs
            if file:
                upload_response = requests.put(presigned_url, data=file.getvalue())

                st.write(file_name + " uploaded")
                st.write("-----------------------------------------------------------")

        except requests.exceptions.RequestException as e:
            st.error(f"An error occurred: {e}")

        # Sleeping for 5 seconds
        time.sleep(30)

        try:
            # Created data for Curl call
            end_point = "https://esmjsglf4h.execute-api.us-west-2.amazonaws.com/dev/v1/?patient_id=2"
            # + text_patient_id
            payload = {}
            headers = {
                'Content-Type': 'application/json'
            }

            response_dynamo = requests.request("get", end_point, headers=headers, data=payload)
            result_dynamo = json.loads(response_dynamo.text)  # Parse JSON response

            print(response_dynamo.text)
            st.write(response_dynamo.text)

        except requests.exceptions.RequestException as e:
            st.error(f"An error occurred: {e}")

    # if file:
    #     with st.spinner("Analyzing data..."):
    # else:
    #     st.warning("Please fill in all fields and upload a file.")
