"""Project-wide error types."""


class BackendError(Exception):
    """Base class for predictable backend failures."""


class ValidationError(BackendError):
    """Raised when a request payload is not acceptable."""


class NotFoundError(BackendError):
    """Raised when a requested entity does not exist."""

