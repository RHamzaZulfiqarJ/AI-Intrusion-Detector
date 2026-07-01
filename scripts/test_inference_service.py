from src.inference.inference_service import InferenceService

from src.llm.explanation_engine import ExplanationEngine

from src.preprocessing.cleaner import DatasetCleaner

from src.preprocessing.encoder import DatasetEncoder

from src.preprocessing.loader import DatasetLoader

from src.preprocessing.scaler import DatasetScaler


def main():

    # -----------------------------
    # Load one real sample
    # -----------------------------

    loader = DatasetLoader()

    df = loader.load()

    cleaner = DatasetCleaner(df)

    df = cleaner.clean()

    encoder = DatasetEncoder(df)

    df = encoder.fit_transform()

    sample = (
        df
        .drop(columns=["Label"])
        .iloc[0]
        .to_dict()
    )
    
    import json

    print(
        json.dumps(
            sample,
            indent=4,
        )
    )

    # -----------------------------
    # Load inference components
    # -----------------------------

    scaler = DatasetScaler()

    scaler.load()

    encoder = DatasetEncoder()

    encoder.load()

    from src.mlops.model_loader import ModelLoader

    model = ModelLoader.load()
    model.eval()

    engine = ExplanationEngine()

    service = InferenceService(

        scaler=scaler,

        encoder=encoder,

        model=model,

        explanation_engine=engine,

    )

    # -----------------------------
    # Predict
    # -----------------------------

    report = service.predict(sample)

    print("=" * 80)

    print(report)


if __name__ == "__main__":

    main()