import pytest
from src.domain.model.fii import FII

@pytest.fixture
def fii_with_forecast():
    """Returns a FII with a forecast value."""
    return FII(
        name="hsml11",
        price=79.5,
        lastIncome=0.74,
        dividendYield=0.94,
        pvp=0.82,
        url="http://example.com",
        forecast=2000.0
    )

def test_fii_should_have_forecast_income(fii_with_forecast):
    "should calc forecast income next month"
    assert fii_with_forecast.forecast == 'R$ 18.50'

def test_fii_should_have_qnt_of_fiis_bought(fii_with_forecast):
    "should calc qnt of fiis buyed"
    assert fii_with_forecast.qnt == 25
