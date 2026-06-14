from ollama import chat


def optimize_resume(
    resume,
    job_description
):

    prompt = f"""
You are an ATS Resume Optimizer.

Optimize the resume according to the job description.

Rules:

- Return ONLY the optimized resume.
- No explanations.
- No notes.
- No comments.
- No conclusions.
- Do not add fake experience.
- Do not add fake companies.
- Do not add fake projects.
- Do not add skills that do not exist.
- Preserve factual correctness.

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
        "Note:",
        "I optimized the resume",
        "This optimized resume",
        "Explanation:",
        "Summary of changes:"
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

    return "\n".join(cleaned_resume).strip()