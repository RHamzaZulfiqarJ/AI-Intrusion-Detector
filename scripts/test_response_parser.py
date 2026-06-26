from src.llm.response_parser import ResponseParser


def main():

    response = """
{
    "attack_name":"DoS_Hulk",
    "confidence":0.998,
    "severity":"High",
    "executive_summary":"A DoS Hulk attack was detected.",
    "technical_explanation":"The observed traffic pattern indicates...",
    "prediction_reason":"High packet rate and abnormal HTTP requests.",
    "mitre_attack":["T1498"],
    "indicators_of_compromise":[
        "High request rate",
        "Resource exhaustion"
    ],
    "business_impact":[
        "Service disruption"
    ],
    "mitigations":[
        "Rate limiting",
        "WAF",
        "Traffic filtering"
    ],
    "references":[
        "MITRE ATT&CK",
        "NIST SP800-61"
    ]
}
"""

    report = ResponseParser.parse(
        response
    )

    print("=" * 60)

    print(report)


if __name__ == "__main__":

    main()