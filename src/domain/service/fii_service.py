from src.domain.scrap.funds_explorer_scraper import FundsExplorerScrapper
from src.domain.repository.fii_repository import FIIRepository

class FIIService:
    def save(self, fiiName: str):
        scrapper = FundsExplorerScrapper()
        fii = scrapper.execute(fiiName)
        
        repository = FIIRepository()
        repository.persist(fii)
        return fii

    def get_all_fii(self):
        repository = FIIRepository()
        fiis_collection = repository.get_all()
        
        if len(fiis_collection) == 0:
            return None
        
        scrapper = FundsExplorerScrapper()
        mapToFiis = lambda fii : scrapper.execute(fii['name'])

        result = map(mapToFiis, fiis_collection)
        return list(result)
        
        
        

        

