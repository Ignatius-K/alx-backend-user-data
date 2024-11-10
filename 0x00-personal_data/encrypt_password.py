#!/usr/bin/env python3

"""Module defines password handling"""

import bcrypt


def hash_password(password: str) -> bytes:
    """Hashes password

    Args:
        password: The password to hash

    Return:
        The hash
    """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(
        password=password.encode(),
        salt=salt
    )


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Checks if password is correct

    Args:
        hashed_password: The password hash
        password: The password to check

    Return:
        True if pasword is valid else False
    """
    return bcrypt.checkpw(
        password=password.encode(),
        hashed_password=hashed_password
    )
