class ValidationError(Exception):
    """Base validation exception."""
    pass


class SchemaValidationError(ValidationError):
    """Raised when dataset schema is invalid."""
    pass


class MissingColumnError(ValidationError):
    """Raised when required columns are missing."""
    pass