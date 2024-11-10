#!/usr/bin/env python3

"""Module defines logger"""

import re
from typing import List




def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """Filters the data"""
    _fields = '|'.join([re.escape(field) for field in fields])
    capture = r'(?P<field>{})=[^{}]*'.format(_fields, re.escape(separator))
    replace = r'\g<field>={}'.format(re.escape(redaction))
    return re.sub(capture, replace, message)


# pattern = r'(?<==).*'

# def filter_datum(
#     fields: List[str], redaction: str,
#     message: str, separator: str
# ) -> str:
#     split_message = message.split(sep=separator)[: -1]
#     for index, datum in enumerate(split_message):
#         if re.findall(r'^.+(?==)', datum)[0] in fields:
#             split_message[index] = re.sub(pattern=pattern,
# repl=redaction, string=datum)
#     return separator.join(split_message)
