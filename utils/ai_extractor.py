from ollama import chat


def extract_ai_skills(text):

    prompt = f"""
You are an ATS parser.

Extract all technical skills from the text.

Include:
- Programming Languages
- Frameworks
- Libraries
- Databases
- Cloud Platforms
- Tools
- Technologies
- AI/ML Skills

STRICT RULES:
- Return only skill names.
- One skill per line.
- No explanations.
- No bullets.
- No numbering.
- No headings.
- No extra text.

Text:

{text}
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

    skills = []

    for line in result.split("\n"):

        line = line.strip()

        if (
            not line
            or line.lower().startswith("here are")
            or line.lower().startswith("skills")
        ):
            continue

        line = line.lstrip("-•*1234567890. ").strip()

        if line and line not in skills:
            skills.append(line)

    return skills