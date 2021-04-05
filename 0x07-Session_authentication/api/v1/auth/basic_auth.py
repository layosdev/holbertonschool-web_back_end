#!/usr/bin/env python3
"""Basic Auth Module"""
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User


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

    def user_object_from_credentials(self, user_email: str, user_pwd: str
                                     ) -> TypeVar('User'):
        """User object from credentials

        Args:
            self ([type]): self

        Returns:
            [type]: User
        """
        if user_email is None or type(user_email) is not str:
            return None

        if user_pwd is None or type(user_pwd) is not str:
            return None

        match = User.search({'email': user_email})

        if len(match) == 0:
            return None

        for user in match:
            if user.is_valid_password(user_pwd):
                return user

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Current user

        Returns:
            [type]: User
        """
        auth_header = self.authorization_header(request)
        authorization = self.extract_base64_authorization_header(auth_header)
        decode_64 = self.decode_base64_authorization_header(authorization)
        credentials = self.extract_user_credentials(decode_64)
        usr = self.user_object_from_credentials(credentials[0], credentials[1])
        return usr
