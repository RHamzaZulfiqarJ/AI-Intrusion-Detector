from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from src.llm.schemas import (
    LLMResponse,
    PromptContext,
)


class BaseLLM(ABC):
    """
    Abstract interface for all LLM providers.
    """

    def __init__(
        self,
        model_name: str,
    ):

        self.model_name = model_name

    @abstractmethod
    def generate(
        self,
        prompt: str,
    ) -> LLMResponse:
        """
        Generate a response from the LLM.
        """
        ...

    @abstractmethod
    def health_check(
        self,
    ) -> bool:
        """
        Check whether the provider is available.
        """
        ...