from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from src.api.scrapper import add_fii
from src.api import scrapper

app = FastAPI()
app.include_router(scrapper.router)
