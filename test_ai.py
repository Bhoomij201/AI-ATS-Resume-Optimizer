from utils.ai_extractor import extract_ai_skills

text = """
Data Analyst

Required Skills

Python
SQL
Power BI
Tableau
Excel
Pandas
NumPy
Machine Learning
Git
GitHub
AWS
"""

skills = extract_ai_skills(text)

print(skills)