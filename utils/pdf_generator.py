from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_summary_pdf(summary, filename="Document_Summary.pdf"):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    title = Paragraph("<b>AI Document Summary</b>", styles["Title"])

    story.append(title)

    story.append(Paragraph("<br/><br/>", styles["BodyText"]))

    story.append(
        Paragraph(summary.replace("\n", "<br/>"), styles["BodyText"])
    )

    doc.build(story)

    return filename