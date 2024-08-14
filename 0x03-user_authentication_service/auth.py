#!/usr/bin/env python3
""" auth.py """
import bcrypt
from typing import bytes


def _hash_password(password: str) -> bytes:
    """Hashes a password using bcrypt and returns the salted hash as bytes."""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)
