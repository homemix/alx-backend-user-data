#!/usr/bin/env python3

def filter_datum(fields: list[str],
                 redaction: str, message: str, separator: str):
    """
    Filter a message based on a list of fields and a redaction string.
    :param fields:
    :param redaction:
    :param message:
    :param separator:
    :return:
    """
    fields_dict = {}
    message_list = message.split(separator)
    for msg in message_list:
        if msg != '':
            key, value = msg.split('=')
            fields_dict[key] = value
            if key in fields:
                fields_dict[key] = redaction
    for key, value in fields_dict.items():
        print(f'{key}={value}', end=';')
