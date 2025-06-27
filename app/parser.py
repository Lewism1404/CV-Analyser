import fitz
import docx
from typing import Dict
from io import BytesIO


def parse_resume(filename: str, content: bytes) -> Dict[str, str]:
    """
    Main function to decide how to read the file.
    It checks the file type and calls the correct helper function.
    """
    if filename.lower().endswith(".pdf"):
        text = extract_text_from_pdf(content)
        return {"text": text}

    elif filename.lower().endswith(".docx"):
        text = extract_text_from_docx(content)
        return {"text": text}

    else:
        return {"error": "Unsupported file type. Please upload a .pdf or .docx file."}


def extract_text_from_pdf(file_bytes: bytes) -> str:
    """
    Extracts all text from a PDF file.
    """
    try:
        doc = fitz.open(stream=file_bytes, filetype="pdf")
        text = ""

        for page in doc:
            text += page.get_text()

        return text.strip()

    except Exception as e:
        return f"Error reading PDF: {str(e)}"


def extract_text_from_docx(file_bytes: bytes) -> str:
    """
    Extracts all text from a DOCX (Word) file.
    """
    try:
        doc = docx.Document(BytesIO(file_bytes))
        text = ""

        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"

        return text.strip()

    except Exception as e:
        return f"Error reading DOCX: {str(e)}"
