#!/usr/bin/env python3
"""
Module defines an implementation of Basic Authentication
"""

from typing import Optional
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Basic Auth implementation

    This inherits from the base Auth implementation
    to add the basic authentication specification

    Attributes:
        PREFIX (str): The prefix of the authorization header

    """
    PREFIX = "Basic "

    def extract_base64_authorization_header(
        self, authorization_header: str
    ) -> Optional[str]:
        """Extract the content of the authorization header

        Args:
            authorization_header: The header to extract

        Return:
            The content of the header
        """
        if (
                not authorization_header or
                not isinstance(authorization_header, str)
        ):
            return None
        if not authorization_header.startswith(self.PREFIX):
            return None
        return authorization_header[len(self.PREFIX):]
