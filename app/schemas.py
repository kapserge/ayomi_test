from datetime import datetime
from typing import List
from pydantic import BaseModel

class CalculBaseSchema(BaseModel):

    notation:str
    resultat :str

    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed = True

class ListCalculResponse(BaseModel):
    status: str
    results: int
    calcul: List[CalculBaseSchema]