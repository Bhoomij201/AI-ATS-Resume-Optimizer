import streamlit as st
from utils.parser import extract_pdf_text
from utils.ai_extractor import extract_ai_skills
# from utils.ats_score import calculate_ats_score
from utils.resume_optimizer import optimize_resume
from utils.suggestions import generate_suggestions
from utils.advanced_ats import calculate_advanced_ats
from utils.resume_parser import parse_resume
from utils.latex_generator import generate_latex
from utils.pdf_generator import generate_resume_pdf
# ----------------------------------
# Page Configuration
# ----------------------------------

st.set_page_config(
    page_title="AI ATS Resume Optimizer",
    page_icon="🤖",
    layout="wide"
)
st.markdown(
    """
    <style>
        .block-container {
            padding-top: 1rem;
            padding-bottom: 1rem;
        }

        h1 {
            font-size: 2.2rem !important;
            margin-bottom: 0rem !important;
        }

        .stCaption {
            font-size: 0.9rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ----------------------------------
# Header
# ----------------------------------

st.markdown(
    """
    <h1>🤖 AI ATS Resume Optimizer</h1>
    """,
    unsafe_allow_html=True
)

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
# ----------------------------------
# Calculate ATS Button
# ----------------------------------

if "analyze_clicked" not in st.session_state:
    st.session_state.analyze_clicked = False

if st.button(
    "🔍 Calculate ATS Score",
    use_container_width=True
):
    st.session_state.analyze_clicked = True

# ----------------------------------
# ATS Analysis
# ----------------------------------
if (
    st.session_state.analyze_clicked
    and resume_text
    and job_description
):

    with st.spinner(
        "AI is analyzing your resume..."
    ):

        resume_skills = extract_ai_skills(
            resume_text
        )

        jd_skills = extract_ai_skills(
            job_description
        )

    # ats_score, matched_skills, missing_skills = calculate_ats_score(
    #     resume_skills,
    #     jd_skills
    # )
    ats_data = calculate_advanced_ats(
    resume_text,
    job_description,
    resume_skills,
    jd_skills
    )

    ats_score = ats_data["final_score"]

    matched_skills = ats_data["matched_skills"]

    missing_skills = list(
        set(jd_skills).difference(
            set(resume_skills)
        )
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
        
        st.subheader("📈 ATS Breakdown")

        b1, b2 = st.columns(2)

        with b1:

            st.write("Skills Match")
            st.progress(
                int((ats_data['skill_score']/50)*100)
            )
            st.caption(
                f"{(ats_data['skill_score']/50)*100:.0f}%"
            )

            st.write("Projects Match")
            st.progress(
                int((ats_data['project_score']/20)*100)
            )
            st.caption(
                f"{(ats_data['project_score']/20)*100:.0f}%"
            )

        with b2:

            st.write("Education Match")
            st.progress(
                int((ats_data['education_score']/10)*100)
            )
            st.caption(
                f"{(ats_data['education_score']/10)*100:.0f}%"
            )

            st.write("Tools Match")
            st.progress(
                int((ats_data['tool_score']/20)*100)
            )
            st.caption(
                f"{(ats_data['tool_score']/20)*100:.0f}%"
            )
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
# AI Resume Optimization
# ----------------------------------

if "optimized_resume" not in st.session_state:
    st.session_state.optimized_resume = ""

if st.button(
    "🚀 Optimize Resume",
    use_container_width=True
):

    with st.spinner(
        "AI is optimizing your resume..."
    ):

        st.session_state.optimized_resume = optimize_resume(
            resume_text,
            job_description
        )

    st.success(
        "Resume Optimized Successfully!"
    )

    # ----------------------------------
    # Resume Preview + TEX Generation
    # ----------------------------------

    if st.session_state.optimized_resume:

        sections = parse_resume(
            st.session_state.optimized_resume
        )
        sections = parse_resume(
           st.session_state.optimized_resume
        )

        st.code(str(sections))
        latex_code = generate_latex(
            sections["summary"],
            sections["education"],
            sections["experience"],
            sections["projects"],
            sections["skills"],
            sections["achievements"]
        )

        with open(
            "generated_resume.tex",
            "w",
            encoding="utf-8"
        ) as file:

            file.write(
                latex_code
            )

        st.subheader(
            "📄 Optimized Resume"
        )

        st.text_area(
            "Generated Resume Content",
            st.session_state.optimized_resume,
            height=450
        )

        st.success(
            "LaTeX Resume Generated Successfully"
        )

        st.info(
            "generated_resume.tex saved in project folder."
        )

    st.divider()

    # ----------------------------------
    # Final Actions
    # ----------------------------------

    col5, col6 = st.columns(2)

    with col5:

        if st.button(
            "🔄 Recalculate ATS",
            use_container_width=True
        ):

            st.info(
                "ATS recalculation will be implemented next."
            )

    with col6:

        if st.button(
            "📥 Download Resume",
            use_container_width=True
        ):

            st.info(
                "PDF generation will be implemented next."
            )