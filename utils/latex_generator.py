def generate_latex(
    summary,
    education,
    experience,
    projects,
    skills,
    achievements
):

    latex = f"""
\\documentclass[11pt,a4paper]{{article}}

\\usepackage[left=0.8in,top=0.8in,right=0.8in,bottom=0.8in]{{geometry}}
\\usepackage[utf8]{{inputenc}}
\\usepackage[T1]{{fontenc}}
\\usepackage[default]{{sourcesanspro}}
\\usepackage{{xcolor}}
\\usepackage{{titlesec}}

\\definecolor{{titleblue}}{{HTML}}{{00199e}}

\\titleformat{{\\section}}{{\\Large\\bfseries\\color{{titleblue}}}}{{}}{{0em}}{{}}

\\begin{{document}}

{{\\Huge \\textbf{{BHOOMI JAIN}}}}

\\vspace{{0.2em}}

9518270384 \\\\
bhoomijainbj201@gmail.com

\\section*{{Personal Profile}}

{summary}

\\section*{{Education}}

{education}

\\section*{{Experience}}

{experience}

\\section*{{Projects}}

{projects}

\\section*{{Skills}}

{skills}

\\section*{{Achievements}}

{achievements}

\\end{{document}}
"""

    return latex