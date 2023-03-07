from pydantic import BaseModel
from decimal import Decimal

class OutputModel(BaseModel):
    class Config:
        orm_mode = True

class FIIOutput(OutputModel):
    name: str
    price: float
    lastIncome: float
    dividendYield: float
    pvp: float
    score: float