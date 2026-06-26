from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from src.rag.document_loader import Document
from src.utils.logger import logger


@dataclass(slots=True)
class Chunk:

    id: int

    category: str

    filename: str

    source: str

    extension: str

    text: str

    start: int

    end: int

    length: int


class TextChunker:

    def __init__(
        self,
        chunk_size: int = 512,
        overlap: int = 64,
    ):

        if overlap >= chunk_size:

            raise ValueError(
                "overlap must be smaller than chunk_size."
            )

        self.chunk_size = chunk_size

        self.overlap = overlap

    def chunk_document(
        self,
        document: Document,
    ) -> list[Chunk]:

        text = document.text.strip()

        if not text:

            return []

        chunks = []

        start = 0

        chunk_id = 0

        step = self.chunk_size - self.overlap
        
        path = Path(document.source)

        category = path.parent.name

        filename = path.stem

        while start < len(text):

            end = min(
                start + self.chunk_size,
                len(text),
            )

            chunks.append(

                Chunk(

                    id=chunk_id,

                    category=category,

                    filename=filename,

                    source=document.source,

                    extension=document.extension,

                    text=text[start:end],

                    start=start,

                    end=end,

                    length=end - start,

                )

            )

            chunk_id += 1

            start += step

        return chunks

    def chunk_documents(
        self,
        documents: list[Document],
    ) -> list[Chunk]:

        all_chunks = []

        for document in documents:

            chunks = self.chunk_document(
                document
            )

            all_chunks.extend(chunks)

        logger.info(
            f"Generated {len(all_chunks)} chunks."
        )

        return all_chunks