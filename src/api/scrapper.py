from fastapi import APIRouter
from pydantic import BaseModel
from src.api.input import FIIInput
from src.api.output import FIIOutput
from src.scrap.funds_exploorer_scraper import FundsExploorerScrapper

router = APIRouter()

@router.post("/fii", tags=["fii"], status_code=201, response_model=FIIOutput, response_model_exclude_unset=True)
async def add_fii(fii: FIIInput):
    """scrap FII and persist it"""
    scrapper = FundsExploorerScrapper()
    return scrapper.execute(fii.name)
