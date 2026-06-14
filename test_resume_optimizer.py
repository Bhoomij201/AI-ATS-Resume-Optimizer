from utils.resume_optimizer import optimize_resume

resume = """
Bhoomi Jain

Skills:
Python
SQL
Machine Learning

Projects:
Built a chatbot using Python.
"""

job_description = """
Need:
Python
SQL
Power BI
Tableau
Pandas
Machine Learning
Git
GitHub
"""

optimized_resume = optimize_resume(
    resume,
    job_description
)

print(optimized_resume)