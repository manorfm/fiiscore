from src.domain.scrap.model.fii import FIIScrapped
from src.domain.scrap.model.indicator import Indicator

def testCreateFII():
    "should create an fii from fii scrapper object"
    indicators: list(Indicator) = []
    indicators.append(Indicator("Liquidez Diária", 31608))
    indicators.append(Indicator("Último Rendimento", 0.74))
    indicators.append(Indicator("Dividend Yield", 0.94))
    indicators.append(Indicator("Patrimônio Líquido", 1500000000.0))
    indicators.append(Indicator("Valor Patrimonial", 96.4))
    indicators.append(Indicator("Rentab. no mês", -0.59))
    indicators.append(Indicator("P/VP", 0.82))
    indicators.append(Indicator("Price", 79.5))

    scrapped = FIIScrapped("hsml11", indicators, 2000.0)
    fii = scrapped.to_fii()

    assert fii.name == "hsml11"
    assert fii.dividendYield == 0.94
    assert fii.lastIncome == 0.74
    assert fii.price == 79.5
    assert fii.pvp == 0.82
    assert fii.forecast == 'R$ 18.50'
    assert fii.qnt == 25