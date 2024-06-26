# DIO - Python - FastAPI - Workout
Projeto "Desenvolvendo sua Primeira API com FastAPI, Python e Docker" da DIO.


## Etapas de desenvolvimento
As etapas de desenvolvimento do projeto foram:

1. Criar um projeto (em PyCharm):

![Image-01-PyCharm](Images/Image-01-PyCharm.png)

2. Executar a aplicação e abrir o navegador em `http://127.0.0.1:8000/`:

![Image-02-Run](Images/Image-02-Run.png)

![Image-03-Hello](Images/Image-03-Hello.png)

3. Verificar se as dependências `fastapi`, `uvicorn`, `sqlalchemy`, `pydantic`, `alembic` e `asyncpg` estão em `requirements.txt`.

4. Criar pacote `contrib` com os arquivos:
- `__init__.py`;
- `schemas.py` que implementa a classe `BaseSchema`:

```python
from pydantic import BaseModel

class BaseSchema(BaseModel):
    class Config:
        extra = 'forbid'
        from_attributes=True
```

- `models.py` que implementa a classe `BaseModel`:

```python
from uuid import uuid4
from sqlalchemy import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID as PG_UUID


class BaseModel(DeclarativeBase):
    id: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True), default=uuid4, nullable=False)
```

Obs: As classes dos outros pacotes herdarão das classes dos arquivos correspondentes do pacote contrib.

5. Criar um pacote para cada entidade no MER, com os arquivos `__init__.py`, `schemas.py` e `models.py`:
- pacote athlete com as classes `Athlete` e `AthleteModel`
- pacote category com as classes `Category` e `CategoryModel`
- pacote training_center com as classes `TrainingCenter` e `TrainingCenterModel`

6. Executar o comando `alembic init`.

7. Criar o arquivo `docker-compose.yml`.


## Referências
DIO - Desenvolvendo sua Primeira API com FastAPI, Python e Docker:
https://web.dio.me/lab/desenvolvendo-uma-api-assincrona-com-fastapi/learning/4058b4b5-1716-43fb-9bf6-121139c16227
| https://github.com/digitalinnovationone/workout_api/tree/main/workout_api

FastAPI - Documentação:
https://fastapi.tiangolo.com/pt/