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

        # Safe float conversion for confidence
        confidence_val = data.get("confidence", 0.0)
        try:
            confidence = float(confidence_val)
        except (ValueError, TypeError):
            confidence = 0.0

        # Safe parsing for mitre_attack list
        mitre_attack_raw = data.get("mitre_attack", [])
        mitre_attack = []
        if isinstance(mitre_attack_raw, list):
            for item in mitre_attack_raw:
                if isinstance(item, dict):
                    tech_id = item.get("technique_id") or item.get("id") or ""
                    tech_name = item.get("technique_name") or item.get("name") or ""
                    tactic = item.get("tactic") or ""
                    url = item.get("url") or ""
                    mitre_attack.append(MitreTechnique(
                        technique_id=tech_id,
                        technique_name=tech_name,
                        tactic=tactic,
                        url=url
                    ))

        # Safe parsing for indicators_of_compromise list
        indicators_raw = data.get("indicators_of_compromise", [])
        indicators_of_compromise = []
        if isinstance(indicators_raw, list):
            for item in indicators_raw:
                if isinstance(item, dict):
                    indicators_of_compromise.append(Indicator(
                        indicator=item.get("indicator") or item.get("type") or "",
                        value=item.get("value") or "",
                        description=item.get("description") or ""
                    ))

        # Safe parsing for business_impact list[str]
        business_impact_raw = data.get("business_impact", [])
        if isinstance(business_impact_raw, list):
            business_impact = [str(item) for item in business_impact_raw if item is not None]
        elif isinstance(business_impact_raw, str):
            business_impact = [business_impact_raw] if business_impact_raw.strip() else []
        else:
            business_impact = []

        # Safe parsing for mitigations list
        mitigations_raw = data.get("mitigations", [])
        mitigations = []
        if isinstance(mitigations_raw, list):
            for item in mitigations_raw:
                if isinstance(item, dict):
                    mitigations.append(Mitigation(
                        title=item.get("title") or "",
                        description=item.get("description") or ""
                    ))

        # Safe parsing for references list
        references_raw = data.get("references", [])
        references = []
        if isinstance(references_raw, list):
            for item in references_raw:
                if isinstance(item, dict):
                    references.append(Reference(
                        title=item.get("title") or "",
                        url=item.get("url") or ""
                    ))

        return SecurityReport(
            attack_name=data.get("attack_name", "Unknown"),
            confidence=confidence,
            severity=data.get("severity", "Unknown"),
            executive_summary=data.get("executive_summary", ""),
            technical_explanation=data.get("technical_explanation", ""),
            prediction_reason=data.get("prediction_reason", ""),
            mitre_attack=mitre_attack,
            indicators_of_compromise=indicators_of_compromise,
            business_impact=business_impact,
            mitigations=mitigations,
            references=references,
        )