import streamlit as st
from utils.parser import extract_pdf_text
from utils.skills import extract_skills

# -------------------------------
# Page Configuration
# -------------------------------

st.set_page_config(
    page_title="AI ATS Resume Optimizer",
    layout="wide"
)

# -------------------------------
# Title
# -------------------------------

st.title("AI ATS Resume Optimizer")

st.write(
    "Upload your resume and optimize it according to the Job Description."
)

# -------------------------------
# Resume Upload
# -------------------------------

st.header("Upload Resume")

uploaded_file = st.file_uploader(
    "Choose your Resume",
    type=["pdf", "docx"]
)

resume_text = ""

if uploaded_file is not None:

    st.success("Resume uploaded successfully!")

    st.write("File Name:", uploaded_file.name)

    if uploaded_file.type == "application/pdf":

        resume_text = extract_pdf_text(uploaded_file)

        st.subheader("Extracted Resume Text")

        st.text_area(
            "Resume Content",
            resume_text,
            height=300
        )

# -------------------------------
# Job Description
# -------------------------------

st.header("Job Description")

job_description = st.text_area(
    "Paste the Job Description here",
    height=250
)

if job_description:

    st.success("Job Description Received Successfully!")

    st.subheader("Job Description Text")

    st.text_area(
        "JD Content",
        job_description,
        height=250
    )

# -------------------------------
# ATS Analysis
# -------------------------------

if resume_text and job_description:

    st.success(
        "Resume and Job Description are ready for ATS Analysis!"
    )

    st.header("Skill Analysis")

    resume_skills = extract_skills(resume_text)

    jd_skills = extract_skills(job_description)

    matched_skills = list(
        set(resume_skills).intersection(
            set(jd_skills)
        )
    )

    missing_skills = list(
        set(jd_skills).difference(
            set(resume_skills)
        )
    )

    # -------------------------------
    # Resume Skills
    # -------------------------------

    st.subheader("Resume Skills")

    for skill in resume_skills:
        st.write("✅", skill)

    # -------------------------------
    # JD Skills
    # -------------------------------

    st.subheader("Job Description Skills")

    for skill in jd_skills:
        st.write("📌", skill)

    # -------------------------------
    # Matched Skills
    # -------------------------------

    st.subheader("Matched Skills")

    if matched_skills:
        for skill in matched_skills:
            st.write("✅", skill)
    else:
        st.warning("No matching skills found.")

    # -------------------------------
    # Missing Skills
    # -------------------------------

    st.subheader("Missing Skills")

    if missing_skills:
        for skill in missing_skills:
            st.write("❌", skill)
    else:
        st.success("No missing skills found!")