#!/usr/bin/env python3
"""
Auth module
"""

from bcrypt import hashpw, gensalt
from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """
    Hash a password
    :param password:
    :return:
    """
    return hashpw(password.encode('utf-8'), gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        user = self._db.find_user_by(email=email)
        if user:
            raise ValueError('user {} already exists'.format(email))
        pwd_hash = _hash_password(password)
        self._db.add_user(email=email, hashed_password=pwd_hash)
        return user
