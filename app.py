import streamlit as st
from utils.parser import extract_pdf_text
from utils.ai_extractor import extract_ai_skills
from utils.ats_score import calculate_ats_score
from utils.resume_optimizer import optimize_resume
from utils.suggestions import generate_suggestions
# ----------------------------------
# Page Configuration
# ----------------------------------

st.set_page_config(
    page_title="AI ATS Resume Optimizer",
    page_icon="🤖",
    layout="wide"
)

# ----------------------------------
# Header
# ----------------------------------

st.title("🤖 AI ATS Resume Optimizer")
st.caption(
    "Upload Resume • Analyze ATS • Optimize Resume with AI"
)

st.divider()

# ----------------------------------
# Upload Section
# ----------------------------------

left, right = st.columns(2)

resume_text = ""
job_description = ""

with left:

    st.subheader("📄 Upload Resume")

    uploaded_file = st.file_uploader(
        "Choose Resume",
        type=["pdf", "docx"]
    )

    if uploaded_file:

        st.success("Resume uploaded successfully!")

        if uploaded_file.type == "application/pdf":

            resume_text = extract_pdf_text(
                uploaded_file
            )

with right:

    st.subheader("📋 Job Description")

    job_description = st.text_area(
        "Paste Job Description",
        height=220
    )

st.divider()

# ----------------------------------
# ATS Analysis
# ----------------------------------

if resume_text and job_description:

    with st.spinner(
        "AI is analyzing your resume..."
    ):

        resume_skills = extract_ai_skills(
            resume_text
        )

        jd_skills = extract_ai_skills(
            job_description
        )

    ats_score, matched_skills, missing_skills = calculate_ats_score(
        resume_skills,
        jd_skills
    )

    # ----------------------------------
    # ATS Score
    # ----------------------------------

    st.header("📊 ATS Score")

    c1, c2 = st.columns([1, 3])

    with c1:

        st.metric(
            "Score",
            f"{ats_score:.2f}%"
        )

    with c2:

        st.progress(
            int(ats_score)
        )

    if ats_score >= 80:

        st.success(
            "Excellent ATS Compatibility"
        )

    elif ats_score >= 60:

        st.warning(
            "Good ATS Compatibility"
        )

    else:

        st.error(
            "Low ATS Compatibility"
        )

    st.divider()

    # ----------------------------------
    # Resume Skills + JD Skills
    # ----------------------------------

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("🧠 Resume Skills")

        if resume_skills:

            st.markdown(
                " ".join(
                    [
                        f"`{skill}`"
                        for skill in resume_skills
                    ]
                )
            )

    with col2:

        st.subheader("📋 JD Skills")

        if jd_skills:

            st.markdown(
                " ".join(
                    [
                        f"`{skill}`"
                        for skill in jd_skills
                    ]
                )
            )

    st.divider()

    # ----------------------------------
    # Matched + Missing
    # ----------------------------------

    col3, col4 = st.columns(2)

    with col3:

        st.subheader("✅ Matched Skills")

        if matched_skills:

            st.markdown(
                " ".join(
                    [
                        f"`{skill}`"
                        for skill in matched_skills
                    ]
                )
            )

    with col4:

        st.subheader("❌ Missing Skills")

        if missing_skills:

            st.markdown(
                " ".join(
                    [
                        f"`{skill}`"
                        for skill in missing_skills
                    ]
                )
            )

    st.divider()
    # ----------------------------------
    # Ai  suggestion
    # ----------------------------------
    st.header("AI Suggestions")

    st.write(
        "Add only those skills that genuinely reflect your knowledge and experience."
    )

    suggestions = generate_suggestions(
        missing_skills
    )

    for skill in suggestions:

        st.write("✔", skill)
    # ----------------------------------
    # Resume Optimization
    # ----------------------------------

    if st.button(
        "🚀 Optimize Resume",
        use_container_width=True
    ):

        with st.spinner(
            "AI is optimizing your resume..."
        ):

            optimized_resume = optimize_resume(
                resume_text,
                job_description
            )

        st.success(
            "Resume Optimized Successfully!"
        )

        st.subheader(
            "📝 Optimized Resume"
        )
        edited_resume = st.text_area(
            "Edit Resume",
            optimized_resume,
            height=450
         )
        if st.button(
            "🔄 Recalculate ATS",
            use_container_width=True
        ):

            st.info(
                "ATS recalculation will be implemented next."
            )
        if st.button(
            "📥 Download Resume",
            use_container_width=True
        ):

            st.info(
                "PDF download feature will be implemented next."
            )
