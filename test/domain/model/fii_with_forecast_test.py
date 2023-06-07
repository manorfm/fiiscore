from src.domain.model.fii import FII

fii = FII("hsml11", price=79.5, dividendYield=0.94, lastIncome=0.74, pvp=0.82, forecast=2000)
score = 0.07

def testFIIShouldHaveForecast():
    "should calc forecast income next month"
    assert fii.forecast == 'R$ 18.50'

def testFIIShouldHaveQnt():
    "should calc qnt of fiis buyed"
    assert fii.qnt == 25
