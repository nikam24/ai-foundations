from pypdf import PdfReader
from docx import Document
from fastapi import UploadFile, HttpException

async def extract_text(file: UploadFile) -> str:
    filename = file.filename.lower()

    if filename.endswith(".pdf"):
        file.file.seek(0)
        reader = PdfReader(file.file)

        pages = []
        for page in reader.pages:
            page_text = page.extract_text() or ""
            pages.append(page_text)

        return "\n".join(pages)

    elif filename.endswith(".docx"):
        file.file.seek(0)
        doc = Document(file.file)

        paragraphs = [p.text for p in doc.paragraphs]
        return "\n".join(paragraphs)

    elif filename.endswith(".txt"):
        file.file.seek(0)
        return file.file.read().decode("utf-8")

    else:
        raise HttpException(
            status_code=400, 
            detail="Unsupported file type. Please upload a PDF, DOCX, or TXT file."
        )