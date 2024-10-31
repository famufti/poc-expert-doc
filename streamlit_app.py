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
    print("----File----")
    st.text_input("----File----")

    # # print(file.getvalue())
    # st.text_input(file.getvalue())
    #
    # f = open(file, 'rb')
    # print(f)
    # st.text_input(f)

    presigned_url = "https://gen-ai-poc1.s3.amazonaws.com/our-expert-doc-poc/patient/4/prescription/b.jpg?AWSAccessKeyId=ASIAS3UDQMI75MGDO4NI&Signature=ME2sSiyRYgH%2FWF%2FessEg14jiWT8%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIQDlDJPZA7mG7oK3vREPbuv2uKtE19N5NONfnFXkF8YpdAIgMOwg3Eo5%2B8IpqponX1GsZZY4Hzd4ksK%2F87z7dhdFZ7EqhQMIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARADGgwxOTY3NzA1NTQ0MzEiDKoJKaL8jq4mMQ3rfSrZAoZcvtRYRP5cFIVufoWHRyw4q7H4mZxfieJAHlCodXbtQ6leBWwSiY%2FfLOHCnuz6FJGw7hVRVTu%2FLI6eZvq5kAqLR8CB8kjbstmnE%2FV2%2B3i8k4eXrm2ahBHNo%2BeYFhxTeYZmEX3GpohShD9GYEeLjg5xVhs%2FM9I2H7e0tJdVwQRAw3gAO%2FnlHGrr%2Fdh49uL0ZmX%2BB3V4iG4JRnWwxTQxFuiKGVJFr2XGU9C0pI3riEwgTqjvDaFHmX2wWzwEMty%2BQyTwS2xxjGA2BUlmbrNCXRIDXlCdcJI2ksOxCbVWoxDaGC3EbyyYo0l8%2FKuHQssySg7wgSRN4VPHOxnqj39EGwQC6Hv6Wzf6zI5Io9ycVBHN17zwauhJuG7DkDseHjxY3kn1XPAFxAyVuF5yKTJW9xRQiiGEYpyMx62vEK%2FpmEqP1884Ju3lq7SDPOfbUiUhOHiuS5JVp%2Fe5jjCWgI25BjqeAf%2FK%2Fm5On7t8%2B%2FyjZJ%2BiU132KTrx2uo26sG60AGEMRv9UVn1nbsqlTEF8axgc7HBWwrHaGppbwdpKEpE6Quwm1WDo2erAUeRPbUa33GCy8T2oAsdfz0yalAtAzz3%2FCBQeIQyHcmsqN08vFS0Hl53jS%2Fb9lj9zDzxD7eMgJfY%2B%2FXltxtbUmmlOAG8ecoIi%2FQ578fMMqWz%2BtZmTBGReIHC&Expires=1730450172"
    upload_response = requests.put(presigned_url, data=file.getvalue())

    # if text_patient_id and text_report_type and text_report_id:

    # endpoint_url = "https://gyjbea39k8.execute-api.us-west-2.amazonaws.com/dev/v1"
    # payload = json.dumps({
    #     "patient_id": text_patient_id,
    #     "report_type": text_report_type,
    #     "report_id": text_report_id
    # })
    # headers = {
    #     'Content-Type': 'application/json'
    # }

    # # Make the curl call (POST request in this case)
    # try:
    #     # response = requests.request("POST", endpoint_url, headers=headers, data=payload)
    #     # st.text_input(response.text)
    #     #
    #     # result = json.loads(response.text)  # Parse JSON response
    #     # body = json.loads(result["body"])
    #     #
    #     # st.text_input(body["url"])
    #
    #     # if file:
    #     print("----File----")
    #     # endpoint_url = body["url"]
    #     endpoint_url = "https://gen-ai-poc1.s3.amazonaws.com/our-expert-doc-poc/patient/4/prescription/b.jpg?AWSAccessKeyId=ASIAS3UDQMI75MGDO4NI&Signature=ME2sSiyRYgH%2FWF%2FessEg14jiWT8%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIQDlDJPZA7mG7oK3vREPbuv2uKtE19N5NONfnFXkF8YpdAIgMOwg3Eo5%2B8IpqponX1GsZZY4Hzd4ksK%2F87z7dhdFZ7EqhQMIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARADGgwxOTY3NzA1NTQ0MzEiDKoJKaL8jq4mMQ3rfSrZAoZcvtRYRP5cFIVufoWHRyw4q7H4mZxfieJAHlCodXbtQ6leBWwSiY%2FfLOHCnuz6FJGw7hVRVTu%2FLI6eZvq5kAqLR8CB8kjbstmnE%2FV2%2B3i8k4eXrm2ahBHNo%2BeYFhxTeYZmEX3GpohShD9GYEeLjg5xVhs%2FM9I2H7e0tJdVwQRAw3gAO%2FnlHGrr%2Fdh49uL0ZmX%2BB3V4iG4JRnWwxTQxFuiKGVJFr2XGU9C0pI3riEwgTqjvDaFHmX2wWzwEMty%2BQyTwS2xxjGA2BUlmbrNCXRIDXlCdcJI2ksOxCbVWoxDaGC3EbyyYo0l8%2FKuHQssySg7wgSRN4VPHOxnqj39EGwQC6Hv6Wzf6zI5Io9ycVBHN17zwauhJuG7DkDseHjxY3kn1XPAFxAyVuF5yKTJW9xRQiiGEYpyMx62vEK%2FpmEqP1884Ju3lq7SDPOfbUiUhOHiuS5JVp%2Fe5jjCWgI25BjqeAf%2FK%2Fm5On7t8%2B%2FyjZJ%2BiU132KTrx2uo26sG60AGEMRv9UVn1nbsqlTEF8axgc7HBWwrHaGppbwdpKEpE6Quwm1WDo2erAUeRPbUa33GCy8T2oAsdfz0yalAtAzz3%2FCBQeIQyHcmsqN08vFS0Hl53jS%2Fb9lj9zDzxD7eMgJfY%2B%2FXltxtbUmmlOAG8ecoIi%2FQ578fMMqWz%2BtZmTBGReIHC&Expires=1730450172"
    #     print(file.getvalue())
    #
    #     files = {"file": file.getvalue()}
    #     # data = {}
    #     print(files)
    #
    #     response_file = requests.post(endpoint_url, files=files)
    #     print(response_file)
    #     # st.text_input(response_file)
    #
    # except requests.exceptions.RequestException as e:
    #     st.error(f"An error occurred: {e}")
    #
    # # if file:
    # #     with st.spinner("Analyzing data..."):
    # # else:
    # #     st.warning("Please fill in all fields and upload a file.")
