#!/usr/bin/env python3
"""
A basic auth class implementation
"""
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
