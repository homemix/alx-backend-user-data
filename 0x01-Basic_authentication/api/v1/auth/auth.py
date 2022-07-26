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
        if excluded_paths is not None:
            if path not in excluded_paths:
                return True
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        if excluded_paths is not None:
            if path in excluded_paths:
                return False
        if path[:-1] in excluded_paths or path+"/" in excluded_paths:
            return False
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
