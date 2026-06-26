from src.llm.explanation_engine import ExplanationEngine
from src.llm.schemas import DetectionContext


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

            "Flow Duration":1250,

            "Flow Bytes/s":65000,

            "Total Fwd Packets":250,

            "Total Backward Packets":3,

        },

    )

    engine = ExplanationEngine()

    report = engine.generate_report(

        detection

    )

    print("="*80)

    print(report)
    

if __name__=="__main__":

    main()