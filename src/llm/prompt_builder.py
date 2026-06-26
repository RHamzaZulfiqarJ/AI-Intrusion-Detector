from __future__ import annotations

from textwrap import dedent

from src.llm.schemas import PromptContext


class PromptBuilder:

    def __init__(self):

        self.system_prompt = dedent(
            """
            You are an expert Cybersecurity Analyst working inside a Security Operations Center (SOC).

            Your expertise includes:

            - Network Intrusion Detection
            - Incident Response
            - Threat Hunting
            - Malware Analysis
            - MITRE ATT&CK Framework
            - NIST Cybersecurity Framework
            - Network Forensics

            Always produce professional security reports.

            Never invent information that is not supported by either
            the prediction results or the retrieved knowledge.

            If confidence is low, explicitly mention that.

            Always respond in Markdown.

            Return the following sections:

            # Executive Summary

            # Technical Explanation

            # Why This Prediction Was Made

            # MITRE ATT&CK Mapping

            # Indicators of Compromise

            # Business Impact

            # Detection Confidence

            # Recommended Mitigations

            # References
            """
        )

    def build(
        self,
        context: PromptContext,
    ) -> str:

        detection = context.detection

        prompt = self.system_prompt

        prompt += "\n\n"

        prompt += "=" * 70

        prompt += "\nNETWORK INTRUSION DETECTION RESULT\n"

        prompt += "=" * 70

        prompt += f"\nAttack Prediction : {detection.prediction}"

        prompt += f"\nConfidence        : {detection.confidence:.4f}"

        prompt += "\n"

        prompt += "\nPrediction Probabilities\n"

        prompt += "-" * 70

        for attack, probability in sorted(

            detection.probabilities.items(),

            key=lambda x: x[1],

            reverse=True,

        ):

            prompt += f"\n{attack:<25} {probability:.4f}"

        prompt += "\n"

        prompt += "\n"

        prompt += "=" * 70

        prompt += "\nNETWORK FLOW FEATURES\n"

        prompt += "=" * 70

        for feature, value in detection.flow_features.items():

            prompt += f"\n{feature:<35} {value}"

        prompt += "\n"

        prompt += "\n"

        prompt += "=" * 70

        prompt += "\nRETRIEVED CYBERSECURITY KNOWLEDGE\n"

        prompt += "=" * 70

        for index, chunk in enumerate(

            context.retrieved_chunks,

            start=1,

        ):

            prompt += "\n"

            prompt += "-" * 70

            prompt += "\n"

            prompt += f"Document {index}\n"

            prompt += f"Category : {chunk.category}\n"

            prompt += f"Source   : {chunk.filename}\n"

            prompt += "\n"

            prompt += chunk.text

            prompt += "\n"

        prompt += "\n"

        prompt += "=" * 70

        prompt += "\nTASK\n"

        prompt += "=" * 70

        prompt += dedent(
            """

            Generate a professional SOC incident report.

            The report must:

            1. Explain the detected attack.

            2. Explain why the IDS predicted this attack.

            3. Reference the retrieved cybersecurity knowledge.

            4. Mention MITRE ATT&CK techniques if applicable.

            5. Mention Indicators of Compromise.

            6. Explain possible business impact.

            7. Recommend mitigation steps.

            8. Mention confidence interpretation.

            9. Use concise professional language.

            Return ONLY valid JSON.

            Do not wrap the JSON inside markdown.

            Do not add explanations.

            Return exactly this schema:

            {
            "attack_name":"",
            "confidence":0.0,
            "severity":"",
            "executive_summary":"",
            "technical_explanation":"",
            "prediction_reason":"",
            "mitre_attack":[
            ],
            "indicators_of_compromise":[
            ],
            "business_impact":[
            ],
            "mitigations":[
            {
            "title":"",
            "description":""
            }
            ],
            "references":[
            {
            "title":"",
            "url":"https://..."
            }
            ]
            }
            """
        )

        return prompt