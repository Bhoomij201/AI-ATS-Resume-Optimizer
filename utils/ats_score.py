def calculate_ats_score(
    resume_skills,
    jd_skills
):

    matched = list(
        set(resume_skills).intersection(
            set(jd_skills)
        )
    )

    missing = list(
        set(jd_skills).difference(
            set(resume_skills)
        )
    )

    if len(jd_skills) > 0:

        score = (
            len(matched)
            /
            len(jd_skills)
        ) * 100

    else:

        score = 0

    return score, matched, missing