#!/usr/bin/env python3

"""Module defines logger"""

import logging
import re
from typing import List

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

    REDACTION = "****"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]) -> None:
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.pii_fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Formats message to hide sensitive data"""
        record.msg = filter_datum(
            self.pii_fields, self.REDACTION, record.msg, self.SEPARATOR)
        return super().format(record)
