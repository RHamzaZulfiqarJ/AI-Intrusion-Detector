from __future__ import annotations

import os
import time

from dotenv import load_dotenv
from google import genai
from google.genai import types

from src.llm.base import BaseLLM
from src.llm.schemas import (
    LLMResponse,
    PromptContext,
)
from src.utils.logger import logger


load_dotenv()


class GeminiLLM(BaseLLM):

    def __init__(self):

        api_key = os.getenv("GEMINI_API_KEY")

        if api_key is None:

            raise ValueError(
                "GEMINI_API_KEY not found in environment."
            )

        model_name = os.getenv(
            "GEMINI_MODEL",
            "gemini-2.5-flash",
        )

        super().__init__(model_name)

        self.client = genai.Client(
            api_key=api_key,
        )

    def health_check(self) -> bool:

        try:

            self.client.models.generate_content(

                model=self.model_name,

                contents="Hello",

                config=types.GenerateContentConfig(
                    max_output_tokens=5,
                ),
            )

            return True

        except Exception as error:

            logger.exception(error)

            return False

    def generate(
        self,
        prompt: str,
    ) -> LLMResponse:

        logger.info(
            "Generating Gemini response..."
        )

        start = time.perf_counter()

        response = self.client.models.generate_content(

            model=self.model_name,

            contents=prompt,

        )

        latency = (
            time.perf_counter()
            - start
        )

        return LLMResponse(

            model_name=self.model_name,

            prompt=prompt,

            response=response.text,

            latency=latency,

        )