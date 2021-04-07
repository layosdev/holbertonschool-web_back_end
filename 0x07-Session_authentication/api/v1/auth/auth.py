#!/usr/bin/env python3
"""Auth Module"""
from flask import request
from typing import List, TypeVar
import os


class Auth:
    """Auth
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Require Auth

        Args:
            path (str): path
            excluded_paths (List[str]): excluded paths

        Returns:
            bool: Status
        """
        if path is not None:
            if path[len(path) - 1] != '/':
                path += '/'
        elif path is None:
            return True
        if path not in excluded_paths:
            return True
        if excluded_paths is None or excluded_paths == '':
            return True
        return False

    def authorization_header(self, request=None) -> str:
        """Authorization header

        Args:
            request ([type], optional): Description. Defaults to None.

        Returns:
            str: Header
        """
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """Current user
        """
        return None

    def session_cookie(self, request=None):
        """[summary]

        Args:
            request ([type], optional): [description]. Defaults to None.
        """

        if request is None:
            return None

        session_name = os.getenv('SESSION_NAME')

        return request.cookies.get(session_name)
