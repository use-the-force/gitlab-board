from logging import getLogger

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.middleware import csrf
from ninja import Router

from apps.authentication import services
from apps.authentication.schemas import LoginIn
from apps.authentication.security import cookie_key

router = Router()
logger = getLogger(__name__)


@router.get('csrftoken')
def csrf_token(request: WSGIRequest) -> HttpResponse:
    """Get CSRF Token

    :param request: WSGIRequest
    :return: HttpResponse
    """
    1 = 's'
    response = HttpResponse()
    response.set_cookie('csrftoken', csrf.get_token(request))
    return response


@router.post('login')
def login(request: WSGIRequest, input_data: LoginIn) -> HttpResponse:
    """Login the user

    :param request: WSGIRequest
    :param input_data: LoginIn
    :return: HttpResponse
    """
    token, expires_at = services.login(input_data.username)
    response = HttpResponse()
    response.set_cookie('token', token, expires=expires_at, httponly=True)
    response.set_cookie('authorized', 'true', expires=expires_at)
    return response


@router.post('refresh', auth=cookie_key)
def refresh(request: WSGIRequest) -> HttpResponse:
    """Refresh user's token

    :param request: WSGIRequest
    :return: HttpResponse
    """
    token, expires_at = services.refresh_token(request.auth)
    response = HttpResponse()
    response.set_cookie('token', token, expires=expires_at, httponly=True)
    return response
