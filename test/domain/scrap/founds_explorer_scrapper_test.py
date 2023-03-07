from src.domain.scrap.funds_explorer_scraper import FundsExplorerScrapper

def testGetHeaderOfFoundsExplorerScrapper():
    "should get the header of fii hgre11 from founds explorer"
    scraper = FundsExplorerScrapper()
    fii = scraper.execute("hgre11")
    assert fii.name == "hgre11"
    #assert fii.price == 0.0
    #assert fii.lastIncome == 0.0
    #assert fii.dividendYield == 0.0
    #assert fii.pvp == 0.0