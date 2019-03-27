"""
SkylabGenesis - Python Client
For more information, visit https://genesis.skylabtech.ai
"""

class SkylabGenesisError(Exception):
    """Base class for SkylabGenesis API errors"""


class AuthenticationError(SkylabGenesisError):
    """API Authentication Failed"""


class APIError(SkylabGenesisError):
    """4xx - Invalid Request (Client error)"""


class ServerError(SkylabGenesisError):
    """5xx - Failed Request (Server error)"""
