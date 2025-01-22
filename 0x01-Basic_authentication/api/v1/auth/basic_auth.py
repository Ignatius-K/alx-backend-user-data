#!/usr/bin/env python3
"""
Module defines an implementation of Basic Authentication
"""

import base64
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

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> Optional[str]:
        """Decodes the content from the base64 header"""
        if (
                not base64_authorization_header or
                not isinstance(base64_authorization_header, str)
        ):
            return None

        encoded_header = base64_authorization_header.encode(encoding='utf-8')
        try:
            base64_decoded_header = base64.b64decode(encoded_header)
            return base64_decoded_header.decode(encoding='utf-8')
        except Exception:
            return None
