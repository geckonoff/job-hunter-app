from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class VacancyBase(BaseModel):
    title: str
    company: str
    description: str
    url: str
    source: str  # e.g. 'email', 'linkedin', 'stepstone'

class VacancyCreate(VacancyBase):
    pass

class Vacancy(VacancyBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
