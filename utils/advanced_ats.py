import re


def calculate_advanced_ats(
    resume_text,
    jd_text,
    resume_skills,
    jd_skills
):

    # ------------------
    # Skills Score (50)
    # ------------------

    if len(jd_skills) > 0:

        matched_skills = list(
            set(resume_skills).intersection(
                set(jd_skills)
            )
        )

        skill_score = (
            len(matched_skills)
            / len(jd_skills)
        ) * 50

    else:

        skill_score = 0

        matched_skills = []

    # ------------------
    # Projects Score (20)
    # ------------------

    project_keywords = [
        "project",
        "developed",
        "built",
        "implemented",
        "designed"
    ]

    project_matches = 0

    for word in project_keywords:

        if word.lower() in resume_text.lower():

            project_matches += 1

    project_score = min(
        project_matches * 4,
        20
    )

    # ------------------
    # Education Score (10)
    # ------------------

    education_keywords = [
        "b.tech",
        "bachelor",
        "computer science",
        "data science",
        "engineering"
    ]

    education_score = 0

    for word in education_keywords:

        if word.lower() in resume_text.lower():

            education_score = 10
            break

    # ------------------
    # Tools Score (20)
    # ------------------

    tool_keywords = [
        "git",
        "github",
        "excel",
        "power bi",
        "tableau",
        "mysql",
        "postgresql"
    ]

    tool_matches = 0

    for word in tool_keywords:

        if (
            word.lower()
            in resume_text.lower()
        ):

            tool_matches += 1

    tool_score = min(
        tool_matches * 3,
        20
    )

    # ------------------
    # Final Score
    # ------------------

    final_score = (
        skill_score
        + project_score
        + education_score
        + tool_score
    )

    final_score = min(
        final_score,
        100
    )

    return {
        "final_score": round(
            final_score,
            2
        ),
        "skill_score": round(
            skill_score,
            2
        ),
        "project_score": round(
            project_score,
            2
        ),
        "education_score": round(
            education_score,
            2
        ),
        "tool_score": round(
            tool_score,
            2
        ),
        "matched_skills":
        matched_skills
    }