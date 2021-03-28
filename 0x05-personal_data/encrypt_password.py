#!/usr/bin/env python3
"""Encrypt password Module"""


import bcrypt


def hash_password(password: str) -> bytes:
    """Hash Password

    Args:
        password (str): password

    Returns:
        bytes: bytes
    """
    passw = bytes(password, 'utf-8')
    encrypt = bcrypt.hashpw(passw, bcrypt.gensalt())
    return encrypt
