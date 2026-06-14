import streamlit as st

st.set_page_config(
    page_title="AI ATS Resume Optimizer",
    layout="wide"
)

st.title("AI ATS Resume Optimizer")

st.write("Upload your resume and optimize it according to the Job Description.")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf", "docx"]
)

if uploaded_file is not None:
    st.success("Resume uploaded successfully!")
    st.write("File Name:", uploaded_file.name)
    st.write("File Type:", uploaded_file.type)