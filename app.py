import streamlit as st
from utils.parser import extract_pdf_text
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

    if uploaded_file.type == "application/pdf":

        resume_text = extract_pdf_text(uploaded_file)

        st.subheader("Extracted Resume Text")

        st.text_area(
            "",
            resume_text,
            height=300
        )