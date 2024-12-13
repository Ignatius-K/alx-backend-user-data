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

        Args:
            path: The path to Checks
            excluded_paths: The paths which don't require authentication

        Return:
            (bool): True if path doesn't require auth else otherwise
        """
        if (
            path is None or excluded_paths is None or
            not isinstance(excluded_paths, List) or
            len(excluded_paths) == 0
        ):
            return True

        path = path if path.endswith('/') else f'{path}/'
        return (path not in excluded_paths)

    def authorization_header(
        self, request: Optional[Request] = None
    ) -> Optional[str]:
        """Gets the authorization header from the request

        Args:
            request: The request

        Return:
            (str | None): The authorization header if exists else None
        """
        if not request or not request.authorization:
            return None

        return request.authorization.to_header()

    def current_user(self, request=None) -> TypeVar('User'):
        """Gets the logged in user
        """
        return None
