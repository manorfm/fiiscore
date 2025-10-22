import pytest
from src.domain.scrap.model.fii import FIIScrapped
from src.domain.scrap.model.indicator import Indicator

@pytest.fixture
def fii_scrapped_data():
    """Provides a list of indicators for a scrapped FII."""
    indicators = [
        Indicator("Liquidez Diária", 31608),
        Indicator("Último Rendimento", 0.74),
        Indicator("Dividend Yield", 0.94),
        Indicator("P/VP", 0.82),
        Indicator("Price", 79.5)
    ]
    return {"name": "hsml11", "url": "http://example.com", "indicators": indicators}

def test_create_fii_from_scrapped_data(fii_scrapped_data):
    """Should create a FII from a FIIScrapped object."""
    # Arrange
    scrapped = FIIScrapped(
        name=fii_scrapped_data["name"],
        indicators=fii_scrapped_data["indicators"],
        url=fii_scrapped_data["url"]
    )

    # Act
    fii = scrapped.to_fii()

    # Assert
    assert fii.name == "hsml11"
    assert fii.dividendYield == 0.94
    assert fii.lastIncome == 0.74
    assert fii.price == 79.5
    assert fii.pvp == 0.82
    assert fii.url == "http://example.com"
