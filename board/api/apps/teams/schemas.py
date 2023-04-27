import datetime

from typing import List

from ninja import Schema
from pydantic import Field


class ColumnSchema(Schema):
    id: int = Field(...)
    name: str = Field(...)
    color: str = Field(...)
    index: int = Field(...)
    gitlab_label_ids: List[int] = Field(...)


class TeamSchema(Schema):
    id: int = Field(...)
    name: str = Field(...)
    columns: List[ColumnSchema] = Field(...)
    created_at: datetime.datetime = Field(...)
    updated_at: datetime.datetime = Field(...)


class GetTeamsOut(Schema):
    data: List[TeamSchema] = Field(...)  # noqa: WPS110


class PostTeamsOut(Schema):
    data: TeamSchema = Field(...)  # noqa: WPS110


class CreateTeamIn(Schema):
    name: str = Field(...)


class GetTeamProjectsOut(Schema):
    data: List[dict] = Field(...)  # noqa: WPS110


class AttachTeamIn(Schema):
    gitlab_project_id: int = Field(...)


class CreateColumnIn(Schema):
    name: str = Field(...)
    color: str = Field(...)


class CreateColumnOut(Schema):
    data: ColumnSchema = Field(...)  # noqa: WPS110


class UpdateColumnIn(Schema):
    name: str = Field(...)
    color: str = Field(...)
    index: int = Field(...)


class AddLabelIn(Schema):
    gitlab_label_id: int = Field(...)
