#!/usr/bin/env python3
"""
An authentication class
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    An authentication class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        require auth method
        :param path:
        :param excluded_paths:
        :return:
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        authorization header method
        :param request:
        :return:
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        get the current user
        :param request:
        :return:
        """
        return None
