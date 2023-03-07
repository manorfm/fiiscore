from src.domain.scrap.funds_explorer_scraper import FundsExplorerScrapper
from src.domain.repository.fii_repository import FIIRepository
from src.domain.repository.fii_duplicated_exception import FIIDuplicatedException
import asyncio
from concurrent.futures import ThreadPoolExecutor

class FIIService:
    def save(self, fiiName: str):
        scrapper = FundsExplorerScrapper()
        fii = scrapper.execute(fiiName)
        
        repository = FIIRepository()
      
        if repository.get(fii) is not None:
            raise FIIDuplicatedException(f"FII {fii.name} is duplicated!")
        
        repository.persist(fii)
        return fii

    def get_all_fii(self):
        repository = FIIRepository()
        fiis_collection = repository.get_all()
        
        if len(fiis_collection) == 0:
            return None
        
        scrapper = FundsExplorerScrapper()
        scrap = lambda fii : scrapper.execute(fii['name'])
        sort = lambda fii: fii.score()

        with ThreadPoolExecutor(max_workers=None) as executor:
             fiis = list(executor.map(scrap, fiis_collection))
             fiis.sort(key=sort, reverse=True)
             return fiis
