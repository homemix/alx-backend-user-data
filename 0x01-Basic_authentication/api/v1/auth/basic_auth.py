#!/usr/bin/env python3
"""
A basic auth class implementation
"""
from base64 import b64decode

from .auth import Auth


class BasicAuth(Auth):
    """
    a Basic auth class implementation
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        extract the base64 authorization header
        :param authorization_header:
        :return:
        """
        if not authorization_header or type(authorization_header) is not str:
            return None

        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header[6:]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str) \
            -> str:
        """
        decode the base64 authorization header
        :param base64_authorization_header:
        :return:
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None

        try:
            encoded = base64_authorization_header.encode('utf-8')
            decoded64 = b64decode(encoded)
            decoded = decoded64.decode('utf-8')
        except BaseException:
            return None

        return decoded
