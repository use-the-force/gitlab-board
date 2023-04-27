from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from ninja import Schema
from pydantic import Field, validator

from apps.users.models import User


class LoginIn(Schema):
    password: str = Field(...)
    username: str = Field(...)

    @validator('username')
    def check_credentials(cls, value: str, values: dict) -> str:  # noqa: WPS110, N805
        """Check user existence

        :param value: value
        :param values: values
        :raises ValidationError: ValidationError
        :return: str

        """
        user = User.objects.filter(username=value).first()

        if not user:
            raise ValidationError(_('Account does not exists'))

        if not user.check_password(values['password']):
            raise ValidationError(_('Wrong password'))

        return value
