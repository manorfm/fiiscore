from pydantic import BaseModel
from decimal import Decimal

class OutputModel(BaseModel):
    class Config:
        orm_mode = True

class FIIOutput(OutputModel):
    name: str
    price: float | None = None
    lastIncome: float | None = None
    dividendYield: float | None = None
    pvp: float | None = None
    score: float | None = None