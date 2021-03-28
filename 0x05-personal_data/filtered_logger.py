#!/usr/bin/env python3
"""Filtered logger Module"""


from typing import List
import re
import logging
import os
import mysql.connector


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


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


def get_logger() -> logging.Logger:
    """Logger

    Returns:
        logging.Logger: Logger
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Conection

    Returns:
        mysql.connector.connection.MySQLConnection: Conection
    """
    conection = mysql.connector.connect(
            user=os.getenv("PERSONAL_DATA_DB_USERNAME"),
            password=os.getenv("PERSONAL_DATA_DB_PASSWORD"),
            host=os.getenv("PERSONAL_DATA_DB_HOST"),
            database=os.getenv("PERSONAL_DATA_DB_NAME")
        )
    return conection


def main():
    """Main
    """
    conection = get_db()
    cursor = conection.cursor()
    cursor.execute("SELECT CONCAT('name=', name, ';ssn=', ssn, ';ip=', ip, \
        ';user_agent', user_agent, ';') AS message FROM users;")
    logger = get_logger()

    for item in cursor:
        logger.log(logging.INFO, item[0])

    cursor.close()
    conection.close()


if __name__ == "__main__":
    main()
