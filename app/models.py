from app.database import Base
from sqlalchemy import TIMESTAMP, Column, String, Boolean,Integer
from sqlalchemy.sql import func


class Calcul(Base):
    __tablename__ = 'calcul'

    id = Column(Integer,primary_key=True, index=True)
    notation = Column(String, index=True)
    resultat = Column (String ,index=True)