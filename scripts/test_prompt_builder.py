from datetime import datetime

from src.llm.prompt_builder import PromptBuilder
from src.llm.schemas import DetectionContext
from src.llm.schemas import PromptContext
from src.rag.retriever import RetrievalResult


def main():

    detection = DetectionContext(

        prediction="DoS_Hulk",

        confidence=0.998,

        probabilities={

            "DoS_Hulk":0.998,

            "BENIGN":0.001,

            "DDoS":0.001,

        },

        flow_features={

            "Flow Duration":1200,

            "Flow Bytes/s":50000,

            "Fwd Packets":120,

        },

        timestamp=datetime.now(),

    )

    retrieved=[

        RetrievalResult(

            score=0.95,

            category="DoS_Hulk",

            filename="mitre_attack",

            source="MITRE",

            text="A DoS attack attempts to exhaust server resources.",

        )

    ]

    context=PromptContext(

        detection=detection,

        retrieved_chunks=retrieved,

    )

    builder=PromptBuilder()

    prompt=builder.build(context)

    print(prompt)


if __name__=="__main__":

    main()