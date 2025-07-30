from sqlalchemy import Column, Integer, String, Text, DateTime
from database import Base
from datetime import datetime

class Vacancy(Base):
    __tablename__ = "vacancies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    company = Column(String)
    description = Column(Text)
    url = Column(String)
    source = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
