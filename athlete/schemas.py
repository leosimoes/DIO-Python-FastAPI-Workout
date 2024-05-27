from typing import Annotated
from pydantic import BaseModel, Field, PositiveInt, PositiveFloat
from contrib.schemas import BaseSchema


class Athlete(BaseSchema):
    name: Annotated[str, Field(description="athlete's name", examples=['Leo'], max_length=50)]
    cpf: Annotated[str, Field(description="athlete's CPF", examples=['12345678900'], max_length=11)]
    age: Annotated[PositiveInt, Field(description="athlete's name", examples=[18])]
    weight: Annotated[PositiveFloat, Field(description="athlete's weight", examples=[75.5])]
    height: Annotated[PositiveFloat, Field(description="athlete's height", examples=[1.70])]
    genre: Annotated[str, Field(description="athlete's genre", examples=['M', 'F'], max_length=1)]
