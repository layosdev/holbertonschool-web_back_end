#!/usr/bin/env python3
"""Basic Auth Module"""
from api.v1.auth.auth import Auth
import base64


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

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """decode

        Args:
            base64_authorization_header (str): header

        Returns:
            str: str
        """
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None

        try:
            encode = base64_authorization_header.encode("utf-8")
            decode_64 = base64.b64decode(encode)
            decodification = decode_64.decode("utf-8")
            return decodification
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """Extract user credentials

        Args:
            self ([type]): self
            str ([type]): decoded

        Returns:
            [type]: str
        """
        if decoded_base64_authorization_header is None:
            return None, None

        if type(decoded_base64_authorization_header) is not str:
            return None, None

        if ':' not in decoded_base64_authorization_header:
            return None, None

        credentials = decoded_base64_authorization_header.split(":")

        return credentials[0], credentials[1]
