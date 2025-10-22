import pytest
from src.domain.scrap.model.fii import FIIScrapped
from src.domain.scrap.model.indicator import Indicator

@pytest.fixture
def fii_scrapped_with_forecast():
    """Provides a FIIScrapped object with a forecast value."""
    indicators = [
        Indicator("Último Rendimento", 0.74),
        Indicator("Dividend Yield", 0.94),
        Indicator("P/VP", 0.82),
        Indicator("Price", 79.5)
    ]
    return FIIScrapped(
        name="hsml11",
        indicators=indicators,
        url="http://example.com",
        forecast=2000.0
    )

def test_create_fii_with_forecast(fii_scrapped_with_forecast):
    """Should create a FII with calculated forecast attributes."""
    # Act
    fii = fii_scrapped_with_forecast.to_fii()

    # Assert
    assert fii.name == "hsml11"
    assert fii.dividendYield == 0.94
    assert fii.lastIncome == 0.74
    assert fii.price == 79.5
    assert fii.pvp == 0.82
    assert hasattr(fii, 'forecast'), "FII should have a 'forecast' attribute"
    assert hasattr(fii, 'qnt'), "FII should have a 'qnt' attribute"
    assert fii.forecast == 'R$ 18.50'
    assert fii.qnt == 25
