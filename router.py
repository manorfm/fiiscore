from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

router = FastAPI()

@router.get("/")
def read_root():
    return {"Hello": "World"}

@router.post("/fii")
def add_fii(input: FIIInput):
    return {"Hello": f"{input.name}"}
