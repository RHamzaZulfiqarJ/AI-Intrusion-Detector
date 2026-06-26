from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pypdf

from src.utils.logger import logger


SUPPORTED_EXTENSIONS = {
    ".txt",
    ".md",
    ".pdf",
}


@dataclass(slots=True)
class Document:

    source: str

    text: str

    extension: str


class DocumentLoader:

    def __init__(

        self,

        knowledge_base_path: str = "data/knowledge_base",

    ):

        self.knowledge_base = Path(
            knowledge_base_path
        )

    def discover_documents(
        self,
    ) -> list[Path]:
        """
        Find all supported documents.
        """

        documents = []

        for file in self.knowledge_base.rglob("*"):

            if (
                file.is_file()
                and file.suffix.lower()
                in SUPPORTED_EXTENSIONS
            ):

                documents.append(file)

        logger.info(
            f"Discovered {len(documents)} documents."
        )

        return sorted(documents)

    def load_document(
        self,
        path: Path,
    ) -> Document:

        suffix = path.suffix.lower()

        if suffix == ".txt":

            text = path.read_text(
                encoding="utf-8",
                errors="ignore",
            )

        elif suffix == ".md":

            text = path.read_text(
                encoding="utf-8",
                errors="ignore",
            )

        elif suffix == ".pdf":

            reader = pypdf.PdfReader(path)

            pages = []

            for page in reader.pages:

                extracted = page.extract_text()

                if extracted:

                    pages.append(extracted)

            text = "\n".join(pages)

        else:

            raise ValueError(
                f"Unsupported document: {path}"
            )

        return Document(

            source=str(path),

            text=text,

            extension=suffix,

        )

    def load_documents(
        self,
    ) -> list[Document]:

        documents = []

        for file in self.discover_documents():

            try:

                document = self.load_document(file)

                documents.append(document)

            except Exception as error:

                logger.exception(
                    f"Failed loading {file}: {error}"
                )

        logger.info(
            f"Loaded {len(documents)} documents."
        )

        return documents