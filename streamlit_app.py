import streamlit as st
import requests
import time
import json


# import time
# 
# def fetch_report_categories(api_url, headers):
#     try:
#         response = requests.get(api_url, headers=headers)
#         data = response.json()
# 
#         if data:  # If data is returned, stop the recursion
#             return data
#         else:
#             time.sleep(5)  # Wait for 5 seconds before the next call
#             return fetch_report_categories(api_url, headers)  # Recursive call
#     except requests.exceptions.RequestException as e:
#         st.error(f"An error occurred: {e}")
#         return None
# 
# # Example usage
# api_url = "https://example.com/api/report-categories"
# headers = {'Content-Type': 'application/json'}
# report_categories = fetch_report_categories(api_url, headers)
# if report_categories:
#     st.write(report_categories)

# Set the page title
st.set_page_config(page_title="Patient's Data Analyzer")

# Page title
st.title("Patient's Data Analyzer")

# Create form for file and text inputs
with st.form("patient_form"):
    file = st.file_uploader("Select a file", type=["jpg", "png", "pdf"])
    text_patient_id = st.text_input("Enter Patient ID")
    # text_report_type = st.text_input("Enter Record Type")

    # Dropdown for selecting an option
    st.title("Select an Record Type")

    options = ["Prescription", "Consultation note", "Discharge summary", "Imaging report", "Laboratory test report", "Pathology report"]
    text_report_type = st.selectbox("Select an Record Type:", options)

    # Display the selected option
    st.write("You selected:", text_report_type)

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

            # st.write(presigned_url)
            # st.write("-----------------------------------------------------------")

            # upload image file to s3 using pre-signed URLs
            if file:
                upload_response = requests.put(presigned_url, data=file.getvalue())

                # st.write(file_name + " uploaded")
                st.write("Patient data submitted...")
                # st.write("-----------------------------------------------------------")

        except requests.exceptions.RequestException as e:
            st.error(f"An error occurred: {e}")

        # Sleeping for 5 seconds
        with st.spinner("Waiting for response..."):
            time.sleep(30)

            try:
                # Created data for Curl call
                end_point = "https://esmjsglf4h.execute-api.us-west-2.amazonaws.com/dev/v1/?patient_id=" + text_patient_id
                payload = {}
                headers = {
                    'Content-Type': 'application/json'
                }

                response_dynamo = requests.request("get", end_point, headers=headers, data=payload)
                result_dynamo = json.loads(response_dynamo.text)  # Parse JSON response

                body_dynamo = result_dynamo["body"]
                # st.write(body_dynamo)
                st.success("Data loaded successfully!")
                st.write("-----------------------------------------------------------")

                for report_category in body_dynamo:
                    st.write(report_category["Report#Category"].removeprefix('prescription#'))
                    st.write("Entities")
                    for entity in report_category["Entities"]:
                        st.write(" - " + entity)
                    st.write("-------------")

            except requests.exceptions.RequestException as e:
                st.error(f"An error occurred: {e}")

    # if file:
    #     with st.spinner("Analyzing data..."):
    # else:
    #     st.warning("Please fill in all fields and upload a file.")
