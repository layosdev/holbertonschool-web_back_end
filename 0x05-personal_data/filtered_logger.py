#!/usr/bin/env python3
"""Filtered logger Module"""


from typing import List
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Filter datum

    Args:
        fields (List[str]): Fields
        redaction (str): Redaction
        message (str): Message
        separator (str): Separator

    Returns:
        str: log message obfuscated
    """
    for item in fields:
        message = re.sub(f'{item}=.*?{separator}',
                         f'{item}={redaction}{separator}', message)
    return message
