from src.scrap.funds_explorer_scraper import FundsExplorerScrapper

def testGetHeaderOfFoundsExplorerScrapper():
    "should get the header of fii hgre11"
    scraper = FundsExplorerScrapper()
    fii = scraper.execute("hgre11")
    assert fii.name == "hgre11"
    assert fii.indicators[0].name == "Liquidez Diária"
    assert fii.indicators[1].name == "Último Rendimento"
    assert fii.indicators[2].name == "Dividend Yield"
    assert fii.indicators[3].name == "Patrimônio Líquido"
    assert fii.indicators[4].name == "Valor Patrimonial"
    assert fii.indicators[5].name == "Rentab. no mês"