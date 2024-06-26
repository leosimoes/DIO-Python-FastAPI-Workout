# DIO - Python - FastAPI - Workout
Project "Developing your First API with FastAPI, Python and Docker" by DIO.


## Development steps
The project development steps were:

1. Create project (in PyCharm):

![Image-01-PyCharm](Images/Image-01-PyCharm.png)

2. Run the application and open the browser at `http://127.0.0.1:8000/`:

![Image-02-Run](Images/Image-02-Run.png)

![Image-03-Hello](Images/Image-03-Hello.png)

3. Check if the dependencies `fastapi`, `uvicorn`, `sqlalchemy`, `pydantic`, `alembic` and `asyncpg` are in `requirements.txt`.

4. Create `contrib` package with the files:
- `__init__.py`;
- `schemas.py` which implements the `BaseSchema` class:

```python
from pydantic import BaseModel

class BaseSchema(BaseModel):
    class Config:
        extra = 'forbid'
        from_attributes=True
```

- `models.py` which implements the `BaseModel` class:

```python
from uuid import uuid4
from sqlalchemy import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID as PG_UUID


class BaseModel(DeclarativeBase):
    id: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True), default=uuid4, nullable=False)
```

Note: The classes in other packages will inherit from the classes in the corresponding files in the contrib package.

5. Create a package for each entity in MER, with the files `__init__.py`, `schemas.py` and `models.py`:
- athlete package with classes `Athlete` and `AthleteModel`
- category package with classes `Category` and `CategoryModel`
- training_center package with classes `TrainingCenter` and `TrainingCenterModel`

6. Run the `alembic init` command.

7. Create the `docker-compose.yml` file.


## References
DIO - Desenvolvendo sua Primeira API com FastAPI, Python e Docker:
https://web.dio.me/lab/desenvolvendo-uma-api-assincrona-com-fastapi/learning/4058b4b5-1716-43fb-9bf6-121139c16227
| https://github.com/digitalinnovationone/workout_api/tree/main/workout_api

FastAPI - Documentation:
https://fastapi.tiangolo.com/