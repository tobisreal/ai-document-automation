from pathlib import Path
from pypdf import PdfReader


def read_txt(path):
    """Extract text from a TXT file."""
    return path.read_text(encoding="utf-8")


def read_pdf(path):
    """Extract text from a text-based PDF."""

    reader = PdfReader(path)

    pages = []

    for page in reader.pages:
        text = page.extract_text()

        if text:
            pages.append(text)

    return "\n".join(pages)


def read_document(file_path):
    """Read supported business document formats."""

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(
            f"Document not found: {file_path}"
        )

    extension = path.suffix.lower()

    if extension == ".txt":
        return read_txt(path)

    elif extension == ".pdf":
        return read_pdf(path)

    else:
        raise ValueError(
            f"Unsupported document type: {extension}"
        )