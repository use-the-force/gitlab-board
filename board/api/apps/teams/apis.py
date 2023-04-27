from logging import getLogger

from django.core.handlers.wsgi import WSGIRequest
from django.http import Http404, HttpResponse
from ninja import Router
from ninja.errors import HttpError

from apps.authentication.security import cookie_key
from apps.core.exceptions import ObjectAlreadyExistsError
from apps.core.status import HTTP422_UNPROCESSABLE_ENTITY, HTTP500_INTERNAL_SERVER_ERROR
from apps.teams import schemas, services

router = Router()
logger = getLogger(__name__)


@router.get('/', auth=cookie_key, response=schemas.GetTeamsOut)
def get_teams(request: WSGIRequest) -> dict:
    """Get teams

    TODO: Needs a pagination

    :param request: WSGIRequest
    :return: dict

    """
    teams = services.get_teams()
    return {
        'data': teams,
    }


@router.post('/', auth=cookie_key, response=schemas.PostTeamsOut)
def create_team(request: WSGIRequest, input_data: schemas.CreateTeamIn) -> dict:
    """Create a team

    :param request: WSGIRequest
    :param input_data: CreateTeamIn
    :return: dict
    :raises HttpError: HttpError

    """
    try:
        team = services.create_team(input_data.name)
    except ObjectAlreadyExistsError as exception:
        logger.exception(exception)
        raise HttpError(HTTP422_UNPROCESSABLE_ENTITY, str(exception))

    return {
        'data': team,
    }


@router.delete('{team_id}', auth=cookie_key)
def delete_team(request: WSGIRequest, team_id: int) -> HttpResponse:
    """Delete a team

    :param request: WSGIRequest
    :param team_id: Team ID
    :raises Http404: Http404
    :raises HttpError: HttpError
    :return: HttpResponse

    """
    try:
        services.delete_team(team_id)
    except Http404 as exception:
        logger.exception(exception)
        raise exception
    except Exception as exception:
        logger.exception(exception)
        raise HttpError(HTTP500_INTERNAL_SERVER_ERROR, str(exception))

    return HttpResponse()


@router.get('{team_id}/projects', auth=cookie_key, response=schemas.GetTeamProjectsOut)
def get_team_projects(request: WSGIRequest, team_id: int) -> dict:
    """Get teams projects

    :param request: WSGIRequest
    :param team_id: Team ID
    :raises Http404: Http404
    :raises HttpError: HttpError
    :return: dict

    """
    try:
        projects = services.get_team_projects(team_id)
    except Http404 as exception:
        logger.exception(exception)
        raise exception
    except Exception as exception:
        logger.exception(exception)
        raise HttpError(HTTP500_INTERNAL_SERVER_ERROR, str(exception))

    return {
        'data': projects,
    }


@router.post('{team_id}/projects', auth=cookie_key)
def attach_project(request: WSGIRequest, team_id: int, input_data: schemas.AttachTeamIn) -> HttpResponse:
    """Attach a team

    :param request: WSGIRequest
    :param team_id: Team ID
    :param input_data: AttachTeamIn
    :raises Http404: Http404
    :raises HttpError: HttpError
    :return: HttpResponse

    """
    try:
        services.attach_project_to_team(team_id, input_data.gitlab_project_id)
    except Http404 as exception:
        logger.exception(exception)
        raise exception
    except ObjectAlreadyExistsError as exception:
        logger.exception(exception)
        raise HttpError(HTTP422_UNPROCESSABLE_ENTITY, str(exception))
    except Exception as exception:
        logger.exception(exception)
        raise HttpError(HTTP500_INTERNAL_SERVER_ERROR, str(exception))

    return HttpResponse()


@router.delete('{team_id}/projects/{gitlab_project_id}', auth=cookie_key)
def delete_project_from_team(request: WSGIRequest, team_id: int, gitlab_project_id: int) -> HttpResponse:
    """Delete a project from team

    :param request: WSGIRequest
    :param team_id: Team ID
    :param gitlab_project_id: GitLab Project ID
    :raises Http404: Http404
    :raises HttpError: HttpError
    :return: HttpResponse

    """
    try:
        services.delete_project_from_team(team_id, gitlab_project_id)
    except Http404 as exception:
        logger.exception(exception)
        raise exception
    except Exception as exception:
        logger.exception(exception)
        raise HttpError(HTTP500_INTERNAL_SERVER_ERROR, str(exception))

    return HttpResponse()


@router.post('{team_id}/columns', auth=cookie_key, response=schemas.CreateColumnOut)
def create_column(request: WSGIRequest, team_id: int, input_data: schemas.CreateColumnIn) -> dict:
    """Create a column for team

    :param request: WSGIRequest
    :param team_id: Team ID
    :param input_data: CreateColumnIn
    :raises Http404: Http404
    :raises HttpError: HttpError
    :return: dict

    """
    try:
        output_data = services.create_column(team_id, input_data.name, input_data.color)
    except Http404 as exception:
        logger.exception(exception)
        raise exception
    except ObjectAlreadyExistsError as exception:
        logger.exception(exception)
        raise HttpError(HTTP422_UNPROCESSABLE_ENTITY, str(exception))
    except Exception as exception:
        logger.exception(exception)
        raise HttpError(HTTP500_INTERNAL_SERVER_ERROR, str(exception))

    return {
        'data': output_data,
    }


@router.patch('{team_id}/columns/{column_id}', auth=cookie_key)
def update_column(request: WSGIRequest, team_id: int, column_id: int, input_data: schemas.UpdateColumnIn) -> HttpResponse:
    """Update the column

    :param request: WSGIRequest
    :param team_id: Team ID
    :param column_id: Column ID
    :param input_data: UpdateColumnIn
    :raises Http404: Http404
    :raises HttpError: HttpError
    :return: HttpResponse

    """
    try:
        services.update_column(column_id, input_data.name, input_data.color, input_data.index)
    except Http404 as exception:
        logger.exception(exception)
        raise exception
    except Exception as exception:
        logger.exception(exception)
        raise HttpError(HTTP500_INTERNAL_SERVER_ERROR, str(exception))

    return HttpResponse()


@router.delete('{team_id}/columns/{column_id}', auth=cookie_key)
def delete_column(request: WSGIRequest, team_id: int, column_id: int) -> HttpResponse:
    """Delete the column

    :param request: WSGIRequest
    :param team_id: Team ID
    :param column_id: Column ID
    :raises Http404: Http404
    :raises HttpError: HttpError
    :return: HttpResponse

    """
    try:
        services.delete_column(column_id)
    except Http404 as exception:
        logger.exception(exception)
        raise exception
    except Exception as exception:
        logger.exception(exception)
        raise HttpError(HTTP500_INTERNAL_SERVER_ERROR, str(exception))

    return HttpResponse()


@router.post('{team_id}/columns/{column_id}/labels', auth=cookie_key)
def add_label(request: WSGIRequest, team_id: int, column_id: int, input_data: schemas.AddLabelIn) -> HttpResponse:
    """Add a label

    :param request: WSGIRequest
    :param team_id: Team ID
    :param column_id: Column ID
    :param input_data: AddLabelIn
    :raises Http404: Http404
    :raises HttpError: HttpError
    :return: HttpResponse

    """
    try:
        services.add_label(team_id, column_id, input_data.gitlab_label_id)
    except Http404 as exception:
        logger.exception(exception)
        raise exception
    except ObjectAlreadyExistsError as exception:
        logger.exception(exception)
        raise HttpError(HTTP422_UNPROCESSABLE_ENTITY, str(exception))
    except Exception as exception:
        logger.exception(exception)
        raise HttpError(HTTP500_INTERNAL_SERVER_ERROR, str(exception))

    return HttpResponse()


@router.delete('{team_id}/columns/{column_id}/labels/{gitlab_label_id}', auth=cookie_key)
def delete_label(request: WSGIRequest, team_id: int, column_id: int, gitlab_label_id: int) -> HttpResponse:
    """Delete the label

    :param request: WSGIRequest
    :param team_id: Team ID
    :param column_id: Column ID
    :param gitlab_label_id: GitLab Label ID
    :raises Http404: Http404
    :raises HttpError: HttpError
    :return: HttpResponse

    """
    try:
        services.delete_label(team_id, column_id, gitlab_label_id)
    except Http404 as exception:
        logger.exception(exception)
        raise exception
    except Exception as exception:
        logger.exception(exception)
        raise HttpError(HTTP500_INTERNAL_SERVER_ERROR, str(exception))

    return HttpResponse()
