from src.llm.schemas import DetectionContext


def main():

    context = DetectionContext(

        prediction="DoS_Hulk",

        confidence=0.998,

        probabilities={
            "DoS_Hulk": 0.998,
            "BENIGN": 0.001,
            "DDoS": 0.001,
        },

        flow_features={
            "Flow Duration": 1023,
            "Total Fwd Packets": 25,
        },
    )

    print("=" * 60)

    print(context)


if __name__ == "__main__":

    main()