from backend.app.services.inference_service import BackendInferenceService


_ai_service: BackendInferenceService | None = None


def set_ai_service(
    service: BackendInferenceService,
):

    global _ai_service

    _ai_service = service


def get_ai_service() -> BackendInferenceService:

    if _ai_service is None:

        raise RuntimeError(
            "Inference service has not been initialized."
        )

    return _ai_service