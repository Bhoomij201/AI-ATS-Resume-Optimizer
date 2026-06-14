import streamlit as st
from utils.parser import extract_pdf_text
from utils.skills import extract_skills

# ----------------------------------
# Page Configuration
# ----------------------------------

st.set_page_config(
    page_title="AI ATS Resume Optimizer",
    layout="wide"
)

# ----------------------------------
# Title
# ----------------------------------

st.title("AI ATS Resume Optimizer")

st.write(
    "Upload your resume and optimize it according to the Job Description."
)

# ----------------------------------
# Resume Upload
# ----------------------------------

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

# ----------------------------------
# Job Description
# ----------------------------------

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

# ----------------------------------
# ATS Analysis
# ----------------------------------

if resume_text and job_description:

    st.success(
        "Resume and Job Description are ready for ATS Analysis!"
    )

    st.header("Skill Analysis")

    # Extract Skills

    resume_skills = extract_skills(resume_text)

    jd_skills = extract_skills(job_description)

    # Matched Skills

    matched_skills = list(
        set(resume_skills).intersection(
            set(jd_skills)
        )
    )

    # Missing Skills

    missing_skills = list(
        set(jd_skills).difference(
            set(resume_skills)
        )
    )

    # ATS Score

    if len(jd_skills) > 0:
        ats_score = (
            len(matched_skills) / len(jd_skills)
        ) * 100
    else:
        ats_score = 0

    # ----------------------------------
    # Resume Skills
    # ----------------------------------

    st.subheader("Resume Skills")

    if resume_skills:
        for skill in resume_skills:
            st.write("✅", skill)
    else:
        st.warning("No skills found.")

    # ----------------------------------
    # JD Skills
    # ----------------------------------

    st.subheader("Job Description Skills")

    if jd_skills:
        for skill in jd_skills:
            st.write("📌", skill)
    else:
        st.warning("No skills found.")

    # ----------------------------------
    # Matched Skills
    # ----------------------------------

    st.subheader("Matched Skills")

    if matched_skills:
        for skill in matched_skills:
            st.write("✅", skill)
    else:
        st.warning("No matching skills found.")

    # ----------------------------------
    # Missing Skills
    # ----------------------------------

    st.subheader("Missing Skills")

    if missing_skills:
        for skill in missing_skills:
            st.write("❌", skill)
    else:
        st.success("No missing skills found!")

    # ----------------------------------
    # ATS Score
    # ----------------------------------

    st.header("ATS Score")

    st.metric(
        label="Resume ATS Score",
        value=f"{ats_score:.2f}%"
    )

    st.progress(int(ats_score))

    if ats_score >= 80:
        st.success("Excellent ATS Compatibility")
    elif ats_score >= 60:
        st.warning("Good ATS Compatibility")
    else:
        st.error("Low ATS Compatibility")