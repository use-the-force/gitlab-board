from datetime import timedelta
from typing import Tuple

import jwt

from django.utils.timezone import now

from apps.users.models import User
from board.settings import JWT_EXPIRATION_DELTA, JWT_SECRET


def get_expiration_delta() -> timedelta:
    """Return expiration delta

    :return: timedelta: timedelta
    """
    return now() + timedelta(seconds=JWT_EXPIRATION_DELTA)


def prepare_user_jwt_payload(user: User) -> dict:
    """Return user JWT payload

    :param user: User
    :return: dict
    """
    return {
        'id': user.id,
        'email': user.email,
        'exp': get_expiration_delta(),
    }


def login(username: str) -> Tuple[str, timedelta]:
    """Return JWT

    :param username: User's username
    :return: Tuple[str, timedelta]
    """
    user = User.objects.get(username=username)
    return encode_jwt(prepare_user_jwt_payload(user)), get_expiration_delta()


def refresh_token(user: User) -> Tuple[str, timedelta]:
    """Return JWT

    :param user: User
    :return: Tuple[str, timedelta]
    """
    return encode_jwt(prepare_user_jwt_payload(user)), get_expiration_delta()


def encode_jwt(payload: dict) -> str:
    """Encode JWT

    :param payload: dict
    :return: str
    """
    return jwt.encode(payload, JWT_SECRET, algorithm='HS256')


def decode_jwt(token: str) -> dict:
    """Decode JWT

    :param token: token
    :return: dict
    """
    return jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
