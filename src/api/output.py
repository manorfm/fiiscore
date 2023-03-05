from pydantic import BaseModel
from decimal import Decimal

class OutputModel(BaseModel):
    class Config:
        orm_mode = True

class FIIIndicatorOutput(OutputModel):
    name: str
    value: Decimal

class FIIOutput(OutputModel):
    name: str
    indicators: list[FIIIndicatorOutput]
    