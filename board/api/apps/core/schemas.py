from ninja import Schema
from pydantic import Field


class PaginationSchema(Schema):
    page: int = Field(...)
    has_next: bool = Field(...)
