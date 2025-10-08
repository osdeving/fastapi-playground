from typing import Optional
from pydantic import BaseModel

class Curso(BaseModel):
    id: Optional[int]
    name: str
    horas: int
    alunos: int
