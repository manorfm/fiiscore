from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from src.domain.api.scrapper import add_fii
from src.domain.api import scrapper

app = FastAPI()
app.include_router(scrapper.router)
