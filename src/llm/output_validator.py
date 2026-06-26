from __future__ import annotations

import json
import re


class OutputValidator:

    @staticmethod
    def clean(response: str) -> str:

        if not response:
            raise ValueError(
                "LLM returned an empty response."
            )

        response = response.strip()

        # Remove ```json
        response = re.sub(
            r"^```json\s*",
            "",
            response,
            flags=re.IGNORECASE,
        )

        # Remove ```
        response = re.sub(
            r"\s*```$",
            "",
            response,
        )

        # Extract first JSON object
        start = response.find("{")

        end = response.rfind("}")

        if start == -1 or end == -1:

            raise ValueError(
                "No JSON object found in LLM response."
            )

        response = response[start:end + 1]

        # Validate JSON

        json.loads(response)

        return response