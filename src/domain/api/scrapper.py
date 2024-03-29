from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.domain.api.input import FIIInput, FIIForecastInput
from src.domain.api.output import FIIOutput, FIIForecastOutput
from src.domain.service.fii_service import FIIService
from src.domain.service.fii_duplicated_exception import FIIDuplicatedException

router = APIRouter()

@router.post("/fii/scrap", tags=["fii"], status_code=201, response_model=FIIOutput, response_model_exclude_unset=True)
async def add_fii(fiiInput: FIIInput) -> FIIOutput:
    """scrap FII and persist it"""
    service = FIIService()
    fii = service.save(fiiInput.name.lower())
    return __to_response_object(fii)

@router.get("/fii/scrap", tags=["fii"], status_code=200, response_model=list[FIIOutput] | None, response_model_exclude_unset=True)
async def get_all_fiis() -> list[FIIOutput] | None:
    """scrap load all fiis persisted and scrap the indicators from this day and ordered by score"""
    service = FIIService()
    fiis = service.get_all_fii()
    return __to_response(fiis)

@router.get("/fii/scrap/forecast", tags=["fii"], status_code=200, response_model=list[FIIForecastOutput] | None, response_model_exclude_unset=True)
async def get_all_fiis(fiiForecast: FIIForecastInput) -> list[FIIOutput] | None:
    """scrap load all fiis persisted and scrap the indicators from this day and ordered by score"""
    service = FIIService()
    fiis = service.get_all_fii_with_forecast(fiiForecast.value)
    return __to_response(fiis)

def __to_response(fiis):
    if fiis is None:
        raise HTTPException(status_code=409, detail="No fii registred.")
    return [*map(lambda fii: __to_response_object(fii), fiis)]
    
def __to_response_object(fii):
    return { **vars(fii), "score": fii.score() }