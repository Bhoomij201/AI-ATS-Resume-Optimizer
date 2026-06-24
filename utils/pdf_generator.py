from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import (
    getSampleStyleSheet,
    ParagraphStyle
)

from reportlab.lib import colors


def generate_resume_pdf(sections):

    doc = SimpleDocTemplate(
        "generated_resume.pdf"
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "Title",
        parent=styles["Title"],
        textColor=colors.darkblue
    )

    heading_style = ParagraphStyle(
        "Heading",
        parent=styles["Heading2"],
        textColor=colors.darkblue
    )

    story = []

    story.append(
        Paragraph(
            "BHOOMI JAIN",
            title_style
        )
    )

    story.append(
        Paragraph(
            "9518270384 | bhoomijainbj201@gmail.com",
            styles["Normal"]
        )
    )

    story.append(
        Spacer(1, 12)
    )

    story.append(
        Paragraph(
            "PROFESSIONAL SUMMARY",
            heading_style
        )
    )

    story.append(
        Paragraph(
            sections["summary"],
            styles["BodyText"]
        )
    )

    story.append(
        Spacer(1, 10)
    )

    story.append(
        Paragraph(
            "EDUCATION",
            heading_style
        )
    )

    story.append(
        Paragraph(
            sections["education"],
            styles["BodyText"]
        )
    )

    story.append(
        Spacer(1, 10)
    )

    story.append(
        Paragraph(
            "PROJECTS",
            heading_style
        )
    )

    story.append(
        Paragraph(
            sections["projects"],
            styles["BodyText"]
        )
    )

    story.append(
        Spacer(1, 10)
    )

    story.append(
        Paragraph(
            "EXPERIENCE",
            heading_style
        )
    )

    story.append(
        Paragraph(
            sections["experience"],
            styles["BodyText"]
        )
    )

    story.append(
        Spacer(1, 10)
    )

    story.append(
        Paragraph(
            "SKILLS",
            heading_style
        )
    )

    story.append(
        Paragraph(
            sections["skills"],
            styles["BodyText"]
        )
    )

    story.append(
        Spacer(1, 10)
    )

    story.append(
        Paragraph(
            "ACHIEVEMENTS",
            heading_style
        )
    )

    story.append(
        Paragraph(
            sections["achievements"],
            styles["BodyText"]
        )
    )

    doc.build(story)