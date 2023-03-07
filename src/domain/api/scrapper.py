from fastapi import APIRouter
from pydantic import BaseModel
from src.domain.api.input import FIIInput
from src.domain.api.output import FIIOutput
from src.domain.service.fii_service import FIIService

router = APIRouter()

@router.post("/fii/scrap", tags=["fii"], status_code=201, response_model=FIIOutput, response_model_exclude_unset=True)
async def add_fii(fii: FIIInput) -> FIIOutput:
    """scrap FII and persist it"""
    service = FIIService()
    return service.save(fii.name)

@router.get("/fii/scrap", tags=["fii"], status_code=200, response_model=list[FIIOutput] | None, response_model_exclude_unset=True)
async def get_all_fiis() -> list[FIIOutput] | None:
    """scrap get all fiis persisted and scrap the indicators today"""
    service = FIIService()
    fiis = service.get_all_fii()
    response = [*map(lambda fii: { **vars(fii), "score": fii.score() }, fiis)]
    
    return response