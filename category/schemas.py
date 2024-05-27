from typing import Annotated
from pydantic import BaseModel, Field, PositiveInt, PositiveFloat
from contrib.schemas import BaseSchema


class Category(BaseSchema):
    name: Annotated[str, Field(description="category's name", examples=['Scale'], max_length=10)]
