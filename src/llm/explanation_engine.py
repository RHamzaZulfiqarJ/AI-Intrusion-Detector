from __future__ import annotations

from src.llm.gemini import GeminiLLM
from src.llm.prompt_builder import PromptBuilder
from src.llm.response_parser import ResponseParser
from src.llm.schemas import (
    DetectionContext,
    PromptContext,
    SecurityReport,
)
from src.rag.retriever import Retriever
from src.llm.output_validator import OutputValidator


class ExplanationEngine:

    def __init__(self):

        self.retriever = Retriever()

        self.prompt_builder = PromptBuilder()

        self.llm = GeminiLLM()

    def generate_report(

        self,

        detection: DetectionContext,

        top_k: int = 5,

    ) -> SecurityReport:

        retrieved_chunks = self.retriever.retrieve(

            query=f"Explain {detection.prediction}",

            category=detection.prediction,

            top_k=top_k,

        )

        prompt_context = PromptContext(

            detection=detection,

            retrieved_chunks=retrieved_chunks,

        )

        prompt = self.prompt_builder.build(

            prompt_context

        )

        response = self.llm.generate(

            prompt

        )

        clean_json = OutputValidator.clean(
            response.response
        )

        report = ResponseParser.parse(
            clean_json
        )

        return report