#!/usr/bin/env python3
"""Session auth"""
from api.v1.auth.auth import Auth
import uuid
from models.user import User


class SessionAuth(Auth):
    """SessionAuth

    Args:
        Auth ([auth]): Auth
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Create session

        Args:
            user_id (str, optional): user_id. Defaults to None.

        Returns:
            str: str
        """
        if user_id is None or type(user_id) is not str:
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """user id for session id

        Args:
            session_id (str, optional): Session id. Defaults to None.

        Returns:
            str: string
        """
        if session_id is None or type(session_id) is not str:
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """Current user

        Args:
            request ([type], optional): request. Defaults to None.
        """
        session_cookie = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_cookie)
        return User.get(user_id)

    def destroy_session(self, request=None):
        """Destroy session

        Args:
            request ([type], optional): request. Defaults to None.

        Returns:
            Bool : Status
        """
        if request is None:
            return False

        session_id = self.session_cookie(request)
        if not session_id:
            return False

        if not self.user_id_for_session_id(session_id):
            return False

        del self.user_id_by_session_id[session_id]
        return True
