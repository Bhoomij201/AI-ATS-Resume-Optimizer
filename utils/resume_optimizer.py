from ollama import chat


def optimize_resume(
    resume,
    job_description
):

    prompt = f"""
You are a professional ATS Resume Writer.

Optimize the resume according to the job description.

You MUST return ALL sections below.

SUMMARY:
(Professional Summary)

SKILLS:
(Skills List)

PROJECTS:
(Project Name
- Point 1
- Point 2)

EDUCATION:
(Education Details)

EXPERIENCE:
(Experience Details)

ACHIEVEMENTS:
(Achievements)

IMPORTANT:

Never skip any section.

If information exists in the resume,
place it in the correct section.

Return ALL sections every time.

Do NOT return only summary and skills.

Do NOT omit projects.

Do NOT omit education.

Do NOT omit experience.

Do NOT omit achievements.

Rules:

1. Use only information already present in the resume.
2. Do not invent experience.
3. Do not invent projects.
4. Do not invent companies.
5. Do not invent achievements.
6. Improve wording and ATS friendliness.
7. Keep information factual.
8. Return ONLY resume content.

Do NOT explain changes.
Do NOT provide notes.
Do NOT provide improvement summary.
Do NOT say "Here is the improved resume".
Do NOT say "I made the following improvements".

Resume:

{resume}

Job Description:

{job_description}
"""

    response = chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    result = response.message.content

    remove_lines = [
        "Here is the optimized resume:",
        "Here is the rewritten resume:",
        "Here is the rewritten summary and skills section:",
        "Rewritten Resume:",
        "Note:",
        "I optimized the resume",
        "This optimized resume",
        "Explanation:",
        "Summary of changes:",
        "I made the following improvements:"
    ]

    cleaned_resume = []

    for line in result.split("\n"):

        skip = False

        for item in remove_lines:

            if line.strip().startswith(item):

                skip = True
                break

        if not skip:
            cleaned_resume.append(line)

    return "\n".join(
        cleaned_resume
    ).strip()