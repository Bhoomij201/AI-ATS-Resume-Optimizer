SKILLS = [
    "python",
    "java",
    "sql",
    "machine learning",
    "deep learning",
    "tensorflow",
    "pytorch",
    "docker",
    "aws",
    "flask",
    "streamlit",
    "react",
    "html",
    "css",
    "javascript",
    "langchain",
    "chromadb",
    "ollama",
    "rag",
    "generative ai",
    "huggingface",
    "vector databases",
    "semantic search",
    "rest api"
]

def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in SKILLS:
        if skill in text:
            found_skills.append(skill)

    return sorted(list(set(found_skills)))