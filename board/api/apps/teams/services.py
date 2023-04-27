from typing import List

from django.shortcuts import get_object_or_404

from apps.core.exceptions import ObjectAlreadyExistsError
from apps.teams.models import Column, ColumnLabel, Project, Team


def get_teams() -> List[dict]:
    """Get teams

    TODO: Needs a pagination

    :return: List[dict]
    """
    teams = Team.objects.all().order_by('name')
    return _get_teams_info(list(teams))


def get_team_projects(team_id: int) -> List[dict]:
    """Get teams projects

    :param team_id: Team ID
    :return: List[dict]
    """
    get_object_or_404(Team, id=team_id)
    projects = Project.objects.filter(team_id=team_id)

    if not projects:
        return []

    return list(projects.values('id', 'gitlab_project_id'))


def delete_team(team_id: int) -> None:
    """Delete a team

    :param team_id: Team ID
    """
    get_object_or_404(Team, id=team_id)
    Team.objects.filter(id=team_id).delete()


def create_team(name: str) -> Team:
    """Create a team

    :param name: Team Name
    :raises ObjectAlreadyExistsError: ObjectAlreadyExistsError
    :return: Team
    """
    if Team.objects.filter(name=name).exists():
        raise ObjectAlreadyExistsError('Object already exists')

    team = Team()
    team.name = name
    team.save()

    return _get_team_info(team)


def attach_project_to_team(team_id: int, gitlab_project_id: int) -> None:
    """Attach project to team

    :param team_id: Team ID
    :param gitlab_project_id: GitLab Project ID
    :raises ObjectAlreadyExistsError: ObjectAlreadyExistsError
    """
    team = get_object_or_404(Team, id=team_id)

    if Project.objects.filter(team_id=team_id, gitlab_project_id=gitlab_project_id).exists():
        raise ObjectAlreadyExistsError('Project already attached')

    project = Project()
    project.team = team
    project.gitlab_project_id = gitlab_project_id
    project.save()


def delete_project_from_team(team_id: int, gitlab_project_id: int) -> None:
    """Delete project from team

    :param team_id: Team ID
    :param gitlab_project_id: GitLab Project ID
    """
    project = get_object_or_404(Project, team_id=team_id, gitlab_project_id=gitlab_project_id)
    Project.objects.filter(id=project.id).delete()


def create_column(team_id: int, name: str, color: str) -> dict:
    """Create a column for team

    :param team_id: Team ID
    :param name: Column Name
    :param color: Column Color
    :return: dict
    """
    team = get_object_or_404(Team, id=team_id)
    last_column = Column.objects.filter(team=team).order_by('-index').first()
    index = 1

    if last_column:
        index = last_column.index + 1

    column = Column()
    column.team = team
    column.name = name
    column.color = color
    column.index = index
    column.save()

    return {
        'id': column.id,
        'name': column.name,
        'color': column.color,
        'index': column.index,
        'gitlab_label_ids': [],
    }


def update_column(column_id: int, name: str, color: str, index: int) -> None:
    """Update the column

    :param column_id: Column ID
    :param name: Column Name
    :param color: Column Color
    :param index: Column Index
    """
    column = get_object_or_404(Column, id=column_id)
    column.name = name
    column.color = color
    column.index = index
    column.save()


def delete_column(column_id: int) -> None:
    """Delete the column and its labels

    :param column_id: Column ID
    """
    get_object_or_404(Column, id=column_id)
    ColumnLabel.objects.filter(column_id=column_id).delete()
    Column.objects.filter(id=column_id).delete()


def add_label(team_id: int, column_id: int, gitlab_label_id: int) -> None:
    """Add a label

    :param team_id: Team ID
    :param column_id: Column ID
    :param gitlab_label_id: GitLab Label ID
    :raises ObjectAlreadyExistsError: ObjectAlreadyExistsError
    """
    get_object_or_404(Team, id=team_id)
    column = get_object_or_404(Column, id=column_id)

    if ColumnLabel.objects.filter(column_id=column_id, gitlab_label_id=gitlab_label_id).exists():
        raise ObjectAlreadyExistsError('Label already attached')

    label = ColumnLabel()
    label.column = column
    label.gitlab_label_id = gitlab_label_id
    label.save()


def delete_label(team_id: int, column_id: int, gitlab_label_id: int) -> None:
    """Delete the label

    :param team_id: Team ID
    :param column_id: Column ID
    :param gitlab_label_id: GitLab Label ID
    """
    get_object_or_404(Team, id=team_id)
    get_object_or_404(Column, id=column_id)
    get_object_or_404(ColumnLabel, column_id=column_id, gitlab_label_id=gitlab_label_id)
    ColumnLabel.objects.filter(column_id=column_id, gitlab_label_id=gitlab_label_id).delete()


def _get_teams_info(teams: list) -> list:
    """Get teams info

    :param teams: List of teams
    :return: list
    """
    team_data = []

    for team in teams:
        team_data.append(_get_team_info(team))

    return team_data


def _get_team_info(team: Team) -> dict:
    """Get team info

    :param team: Team
    :return: dict
    """
    columns = Column.objects.filter(team=team).order_by('index')
    column_data = []

    for column in columns:
        labels = list(ColumnLabel.objects.filter(column=column).values_list('gitlab_label_id', flat=True))
        column_data.append({
            'id': column.id,
            'name': column.name,
            'color': column.color,
            'index': column.index,
            'gitlab_label_ids': labels,
        })

    return {
        'id': team.id,
        'name': team.name,
        'columns': column_data,
        'created_at': team.created_at,
        'updated_at': team.updated_at,
    }
