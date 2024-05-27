from typing import Annotated
from pydantic import BaseModel, Field, PositiveInt, PositiveFloat
from contrib.schemas import BaseSchema


class TrainingCenter(BaseSchema):
    name: Annotated[str, Field(description="training center's name", examples=['Scale'], max_length=10)]
    address: Annotated[str, Field(description="training center's address", example='Main street', max_length=60)]
    owner: Annotated[str, Field(description="training center's owner", example='Leonardo', max_length=30)]
