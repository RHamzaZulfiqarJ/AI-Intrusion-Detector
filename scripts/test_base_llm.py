from __future__ import annotations

import time

from src.llm.base import BaseLLM
from src.llm.schemas import (
    DetectionContext,
    LLMResponse,
    PromptContext,
)


class DummyLLM(BaseLLM):

    def __init__(self):

        super().__init__("dummy")

    def generate(
        self,
        prompt: str,
    ) -> LLMResponse:

        return LLMResponse(

            model_name=self.model_name,

            prompt=prompt,

            response="Dummy response",

            latency=0.01,

        )

    def health_check(
        self,
    ):

        return True

    def build_prompt(
        self,
        context: PromptContext,
    ):

        return f"Attack: {context.detection.prediction}"


def main():

    detection = DetectionContext(

        prediction="DoS_Hulk",

        confidence=0.99,

        probabilities={},

        flow_features={},

    )

    context = PromptContext(

        detection=detection,

        retrieved_chunks=[],

    )

    llm = DummyLLM()

    prompt = llm.build_prompt(context)

    response = llm.generate(prompt)

    print("=" * 60)

    print(prompt)

    print()

    print(response)


if __name__ == "__main__":

    main()