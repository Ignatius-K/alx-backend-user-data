#!/usr/bin/env python3
"""Module defines the Authentication implementation
"""

from flask import Request
from typing import List, Optional, TypeVar


class Auth:
    """
    Auth class that defines the authentication of the API

    It defines the base implementation for other Authentication
    types
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks if request requires authentication
        """
        return False

    def authorization_header(
        self, request: Optional[Request] = None
    ) -> Optional[str]:
        """Gets the authentication header from the request
        """
        return None

    def current_user(self, request: Optional[Request] = None) -> TypeVar('User'):
        """Gets the logged in user
        """
        return None
