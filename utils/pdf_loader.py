import fitz  # PyMuPDF

def load_pdf(uploaded_file):
    """
    Extract text from a single PDF
    """
    pdf = fitz.open(stream=uploaded_file.read(), filetype="pdf")

    text = ""

    for page in pdf:
        text += page.get_text()

    return text


def load_multiple_pdfs(uploaded_files):
    """
    Extract text from multiple PDFs
    """

    combined_text = ""

    for file in uploaded_files:

        file.seek(0)

        pdf = fitz.open(stream=file.read(), filetype="pdf")

        for page in pdf:
            combined_text += page.get_text() + "\n"

    return combined_text