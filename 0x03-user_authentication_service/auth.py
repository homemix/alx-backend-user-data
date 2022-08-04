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
from typing import Union


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

    def get_user_from_session_id(self, session_id: str) -> Union[str, None]:
        """
        get user by session
        :param session_id:
        :return:
        """
        if session_id is None:
            return None

        try:
            user = self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None

        return user

    def destroy_session(self, user_id: int) -> None:
        """
        destroy session for user
        :param user_id:
        :return:
        """
        self._db.update_user(user_id, session_id=None)

    def get_reset_password_token(self, email: str) -> str:
        """
        get reset password token
        :param email:
        :return:
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError()

        if user:
            reset_token = _generate_uuid()
            self._db.update_user(user.id, reset_token=reset_token)
        return reset_token

    def update_password(self, reset_token: str, password: str) -> None:
        """
        update password
        :param reset_token:
        :param password:
        :return:
        """
        if reset_token is None or password is None:
            return None
        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            raise ValueError

        if user:
            pwd_hash = _hash_password(password)
            self._db.update_user(user.id,
                                 hashed_password=pwd_hash, reset_token=None)
