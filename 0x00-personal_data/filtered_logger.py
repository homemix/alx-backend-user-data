#!/usr/bin/env python3
"""
re sub for personal data
"""
import re
from typing import List


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str, separator: str) -> str:
    """
    Filter a message based on a list of fields and a redaction string.
    """
    for f in fields:
        message = re.sub(f'{f}=.*?{separator}',
                         f'{f}={redaction}{separator}', message)
    return message
