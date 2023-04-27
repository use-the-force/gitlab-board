from logging import getLogger
from typing import Dict

from django.core.handlers.wsgi import WSGIRequest
from django.forms import model_to_dict
from ninja import Router

from apps.authentication.security import cookie_key
from apps.users.schemas import GetMeOut

router = Router()
logger = getLogger(__name__)


@router.get('me', auth=cookie_key, response=GetMeOut)
async def get_user(request: WSGIRequest) -> Dict:
    """Get user info

    :param request: WSGIRequest
    :return: Dict
    """
    return model_to_dict(request.auth)
