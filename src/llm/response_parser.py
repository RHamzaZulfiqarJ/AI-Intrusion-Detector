from __future__ import annotations

import json

from src.llm.schemas import MitreTechnique, Reference, SecurityReport, Indicator, Mitigation
from src.llm.output_validator import OutputValidator


class ResponseParser:

    @staticmethod
    def parse(
        response: str,
    ) -> SecurityReport:

        response = OutputValidator.clean(response)

        data = json.loads(response)

        return SecurityReport(

            attack_name=data.get(
                "attack_name",
                "Unknown",
            ),

            confidence=float(
                data.get(
                    "confidence",
                    0.0,
                )
            ),

            severity=data.get("severity", "Unknown"),

            executive_summary=data.get("executive_summary", ""),

            technical_explanation=data.get("technical_explanation", ""),

            prediction_reason=data.get("prediction_reason", ""),

            mitre_attack = [

                MitreTechnique(**item)

                for item in data.get("mitre_attack", [])

            ],

            indicators_of_compromise=[

                Indicator(**item)

                for item in data.get(
                    "indicators_of_compromise",
                    [],
                )

            ],

            business_impact=data.get("business_impact", ""),

            mitigations = [

                Mitigation(**item)

                for item in data.get("mitigations", [])

            ],

            references = [

                Reference(**item)

                for item in data.get("references", [])

            ]
        )