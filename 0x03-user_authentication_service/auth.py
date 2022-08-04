#!/usr/bin/env python3
"""
Auth module
"""
import uuid

import bcrypt
from bcrypt import hashpw, gensalt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """
    Hash a password
    :param password:
    :return:
    """
    return hashpw(password.encode('utf-8'), gensalt())


def _generate_uuid() -> str:
    """Returns a string representation of a new UUID"""
    return str(uuid.uuid4())


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
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        if user:
            if bcrypt.checkpw(password.encode('utf-8'), user.hashed_password):
                return True
        return False

    def create_session(self, email: str) -> str:
        """
        create session for user
        :param email:
        :return:
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        if user:
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
        return session_id
