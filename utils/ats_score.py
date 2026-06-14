def calculate_ats_score(
    resume_skills,
    jd_skills
):

    # Convert to lowercase

    resume_set = set(
        skill.strip().lower()
        for skill in resume_skills
    )

    jd_set = set(
        skill.strip().lower()
        for skill in jd_skills
    )

    # ----------------------------
    # Synonym Dictionary
    # ----------------------------

    synonyms = {

        "ml": "machine learning",
        "machine learning": "machine learning",

        "ai": "artificial intelligence",
        "artificial intelligence": "artificial intelligence",

        "js": "javascript",
        "javascript": "javascript",

        "reactjs": "react",
        "react": "react",

        "nodejs": "node.js",
        "node.js": "node.js",

        "postgres": "postgresql",
        "postgresql": "postgresql",

        "mysql": "mysql",

        "gcp": "google cloud",
        "google cloud": "google cloud",

        "aws": "aws",

        "git": "git",
        "github": "github",

        "numpy": "numpy",
        "pandas": "pandas",

        "powerbi": "power bi",
        "power bi": "power bi",

        "tableau": "tableau",

        "sql": "sql",
        "python": "python"
    }

    normalized_resume = set()

    for skill in resume_set:

        if skill in synonyms:
            normalized_resume.add(
                synonyms[skill]
            )
        else:
            normalized_resume.add(
                skill
            )

    normalized_jd = set()

    for skill in jd_set:

        if skill in synonyms:
            normalized_jd.add(
                synonyms[skill]
            )
        else:
            normalized_jd.add(
                skill
            )

    # ----------------------------
    # Matching
    # ----------------------------

    matched = list(
        normalized_resume.intersection(
            normalized_jd
        )
    )

    missing = list(
        normalized_jd.difference(
            normalized_resume
        )
    )

    # ----------------------------
    # ATS Score
    # ----------------------------

    if len(normalized_jd) == 0:

        score = 0

    else:

        score = (
            len(matched)
            /
            len(normalized_jd)
        ) * 100

    matched.sort()
    missing.sort()

    return score, matched, missing