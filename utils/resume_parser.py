def parse_resume(text):

    sections = {
        "summary": "",
        "education": "",
        "experience": "",
        "projects": "",
        "skills": "",
        "achievements": ""
    }

    current = None

    for line in text.splitlines():

        line = line.strip()

        line = line.replace("**", "")

        if line.startswith("SUMMARY:"):
            current = "summary"
            continue

        elif line.startswith("SKILLS:"):
            current = "skills"
            continue

        elif line.startswith("PROJECTS:"):
            current = "projects"
            continue

        elif line.startswith("EDUCATION:"):
            current = "education"
            continue

        elif line.startswith("EXPERIENCE:"):
            current = "experience"
            continue

        elif line.startswith("ACHIEVEMENTS:"):
            current = "achievements"
            continue

        if current:
            sections[current] += line + "\n"

    return sections