#!/usr/bin/env python3
"""file to encrypt password"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hash a password.
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Check if a password is valid.
    """
    return bcrypt.checkpw(password.encode(), hashed_password)
