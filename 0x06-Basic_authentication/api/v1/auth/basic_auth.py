#!/usr/bin/env python3
"""Basic Auth Module"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """BasicAuth

    Args:
        Auth ([type]): Auth
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Base64

        Args:
            authorization_header (str): Header

        Returns:
            str: str
        """
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if authorization_header[0:6] != 'Basic ':
            return None
        return authorization_header[6:]
