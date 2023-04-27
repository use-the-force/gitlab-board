from ninja import Schema
from pydantic import Field


class GetMeOut(Schema):
    id: int = Field(...)
    first_name: str = Field(...)
    last_name: str = Field(...)
    username: str = Field(...)
    email: str = Field(...)
