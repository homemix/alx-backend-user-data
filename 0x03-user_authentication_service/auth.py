#!/usr/bin/env python3
"""
Auth module
"""

from bcrypt import hashpw, gensalt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


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
        """
        register new user
        :param email:
        :param password:
        :return:
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists.")
        except NoResultFound:
            pwd_hash = _hash_password(password)
            new_user = self._db.add_user(email=email, hashed_password=pwd_hash)
            return new_user

    def valid_login(self, email: str, password: str) -> bool:
        """
        validate user login
        :param email:
        :param password:
        :return:
        """
        user = self._db.find_user_by(email=email)
        if user:
            if user.hashed_password == _hash_password(password):
                return True
        return False
