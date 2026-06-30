import fitz

from app.services.chunker import split_text


class PDFLoader:
    """
    Reads a PDF and splits it into chunks.
    """

    def load_pdf(self, pdf_path: str) -> str:
        document = fitz.open(pdf_path)

        text = ""

        for page in document:
            text += page.get_text()

        document.close()

        return text

    def load_and_chunk(self, pdf_path: str) -> list[str]:
        text = self.load_pdf(pdf_path)

        chunks = split_text(text)

        return chunks