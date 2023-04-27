from typing import Optional

from jwt import DecodeError, ExpiredSignatureError
from ninja.security import APIKeyCookie

from apps.authentication.services import decode_jwt
from apps.users.models import User


class CookieKey(APIKeyCookie):
    param_name = 'token'

    def authenticate(self, request, key) -> Optional[User]:
        """Authenticate user

        :param request: WSGIRequest
        :param key: secret key
        :return: Optional[User]

        """
        try:
            payload = decode_jwt(key)
        except (DecodeError, ExpiredSignatureError):
            return None

        return User.objects.filter(id=payload['id']).first()


cookie_key = CookieKey()
