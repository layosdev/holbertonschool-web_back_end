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


def is_valid(hashed_password: bytes, password: str) -> bool:
    """validate

    Args:
        hashed_password (bytes): bytes
        password (str): password

    Returns:
        bool: status
    """
    status = bcrypt.checkpw(bytes(password, 'utf-8'), hashed_password)
    return status
