#!/usr/bin/env python3

"""Module defines logger"""

import mysql.connector
import logging
import re
from os import environ
from typing import Iterable, List

PII_FIELDS = (
    "name",
    "email",
    "phone",
    "ssn",
    "password"
)

p = {
    'cap': lambda x, y: r'(?P<field>{})=[^{}]*'.format(x, y),
    'rep': lambda x: r'\g<field>={}'.format(x)
}


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """Filters the data"""
    _fields = '|'.join([re.escape(field) for field in fields])
    capture, replace = p['cap'](_fields, separator), p['rep'](redaction)
    return re.sub(capture, replace, message)


class RedactingFormatter(logging.Formatter):
    """RedactingFormatter
    Formats the logs to hide sensitive information

    Attributes:
        REDACTION: The string to replace sensitive info with
        FORMAT: The format of the log
        SEPARATOR: The string that separates the data in log
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: Iterable[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.pii_fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Formats message to hide sensitive data"""
        record.msg = filter_datum(
            list(self.pii_fields), self.REDACTION, record.msg, self.SEPARATOR)
        return super().format(record)


def get_logger() -> logging.Logger:
    """Builds a logger"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    # define handler
    stream_handler = logging.StreamHandler()
    logger.addHandler(stream_handler)

    # add redaction Formatter
    formatter = RedactingFormatter(PII_FIELDS)
    if logger.hasHandlers():
        for handler in logger.handlers:
            handler.setFormatter(formatter)

    return logger

def get_db() -> mysql.connector.connection.MySQLConnection:
    """ Returns a connector to a MySQL database """
    username = environ.get("PERSONAL_DATA_DB_USERNAME", "root")
    password = environ.get("PERSONAL_DATA_DB_PASSWORD", "")
    host = environ.get("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = environ.get("PERSONAL_DATA_DB_NAME")

    cnx = mysql.connector.connection.MySQLConnection(user=username,
                                                     password=password,
                                                     host=host,
                                                     database=db_name)
    return cnx
