from pydantic import BaseModel

class FIIInput(BaseModel):
    name: str

class FIIForecastInput(BaseModel):
    value: float
