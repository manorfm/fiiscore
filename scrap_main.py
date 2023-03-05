from scrap.scraper import ScrapperFII
from scrap.fii_not_fount_exception import FIINotFoundException

scrapperFII = ScrapperFII()

#URL = "https://www.fundsexplorer.com.br/funds/hgre11"
#URL = "https://www.fundsexplorer.com.br/funds/aiec11"

fii = "hgre11"

try:
    fii = indicators = scrapperFII.execute(fii)
    print(fii)
except FIINotFoundException as inst:
    print(inst.message)
