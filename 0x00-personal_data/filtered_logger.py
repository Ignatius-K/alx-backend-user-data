#!/usr/bin/env python3

"""Module defines logger"""

import re
from typing import List

reg = r'(?:{})=(.+?)(?:{})'


def filter_datum(
    fields: List, redaction: str, message: str, separator: str
) -> str:
    """Filters the data"""
    r_fields = '|'.join([re.escape(field) for field in fields])
    data = re.findall(reg.format(r_fields, re.escape(separator)), message)
    return re.sub(pattern='|'.join(data), repl=redaction, string=message)


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
