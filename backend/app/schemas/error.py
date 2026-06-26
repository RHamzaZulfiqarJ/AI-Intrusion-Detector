from pydantic import BaseModel


class ErrorResponse(BaseModel):

    success: bool = False

    request_id: str | None = None

    error: str

    message: str