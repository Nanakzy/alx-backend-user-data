#!/usr/bin/env python3
""" auth.py """
import bcrypt
from typing import optional
from db import DB
from user import User
import uuid


def _hash_password(password: str) -> bytes:
    """
    Hashes the provided password with bcrypt & return hashed password as bytes.
    Args:
        password (str): The password to hash.

    Returns:
        bytes: The hashed password.
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registers a new user if email is not already registered."""
        try:
            existing_user = self._db.find_user_by_email(email)
            if existing_user:
                raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            new_user = self._db.add_user(email, hashed_password)
            return new_user

    def valid_login(self, email: str, password: str) -> bool:
        """Validate the email and password."""
        try:
            user = self._db.find_user_by_email(email)
            return bcrypt.checkpw(
                password.encode('utf-8'), user.hashed_password)
        except NoResultFound:
            return False

    def _generate_uuid() -> str:
        """Generate a new UUID and return its string representation."""
        return str(uuid.uuid4())
