#!/usr/bin/env python3
"""
auth module
"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt's hashpw function.

    Args:
        password (str): The password to be hashed.

    Returns:
        bytes: A salted hash of the input password.
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password
