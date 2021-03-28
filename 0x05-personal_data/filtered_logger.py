#!/usr/bin/env python3
"""Filtered logger Module"""


from typing import List
import re
import logging


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


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Constructor
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Format

        Args:
            record (logging.LogRecord): Args

        Returns:
            str: Description
        """
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)
