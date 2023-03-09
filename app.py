from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.responses import PlainTextResponse

from src.domain.api.scrapper import add_fii
from src.domain.api import scrapper
from src.domain.service.fii_duplicated_exception import FIIDuplicatedException
from src.domain.scrap.fii_not_fount_exception import FIINotFoundException

app = FastAPI()
app.include_router(scrapper.router)

@app.exception_handler(FIIDuplicatedException)
async def duplicated_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=409)

@app.exception_handler(FIINotFoundException)
async def fii_notfound_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=409)
