from src.domain.model.fii import FII

fii = FII("hsml11", price=79.5, dividendYield=0.94, lastIncome=0.74, pvp=0.82)
score = 10.67

def testCalculateScoreOfFII():
    "should calculate the score of fii"
    assert fii.score() == score

def testFIIScoreWhenDividendYieldDownTheScoreDown():
    "should score down when dividend yield down"
    fii.dividendYield = 0.91
    assert fii.score() < score

def testFIIScoreWhenLastIncomeDownTheScoreDown():
    "should score down when last income down"
    fii.lastIncome = 0.69
    assert fii.score() < score

def testFIIScoreWhenPVPDownTheScoreUP():
    "should score down when pvp up"
    fii.pvp = 0.86
    assert fii.score() < score

def testFIIScoreWhenPriceDownTheScoreUP():
    "should score down when price up"
    fii.price = 82.2
    assert fii.score() < score