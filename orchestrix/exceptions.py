class OrchestrixError(Exception):
    """Base class for Orchestrix exceptions."""

class ConnectionError(OrchestrixError):
    """Raised when orchestrix cannot connect to a host."""

class AuthenticationError(OrchestrixError):
    """Raised when authentication fails during SSH connection."""

class HostNotFoundError(OrchestrixError):
    """Raised when a specified host is not found in the inventory."""

class ModuleNotFoundError(OrchestrixError):
    """Raised when a specified module does not exist."""