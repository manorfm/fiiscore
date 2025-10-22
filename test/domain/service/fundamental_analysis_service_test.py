import pytest
from src.domain.model.fii import FII
from src.domain.service.fundamental_analysis_service import FundamentalAnalysisService

@pytest.fixture
def ideal_fii():
    """Returns a FII with ideal indicators."""
    return FII(
        name="GOOD FII",
        price=100.0,
        lastIncome=1.2,
        dividendYield=1.2,  # 1.2%
        pvp=0.9,
        url="http://example.com",
        daily_liquidity=1500000.0,
        vacancy=0.0,
        asset_amount=12
    )

@pytest.fixture
def bad_fii():
    """Returns a FII with bad indicators."""
    return FII(
        name="BAD FII",
        price=120.0,
        lastIncome=0.5,
        dividendYield=0.5,
        pvp=1.8,
        url="http://example.com",
        daily_liquidity=50000.0,
        vacancy=0.3, # 30%
        asset_amount=1
    )

def test_get_analysis_for_ideal_fii(ideal_fii):
    # Arrange
    analysis_service = FundamentalAnalysisService()

    # Act
    analysis = analysis_service.get_analysis(ideal_fii)

    # Assert
    assert "score" in analysis
    assert "classification" in analysis
    assert analysis['score'] > 0.75
    assert analysis['classification'] == "Recomendado"

def test_get_analysis_for_bad_fii(bad_fii):
    # Arrange
    analysis_service = FundamentalAnalysisService()

    # Act
    analysis = analysis_service.get_analysis(bad_fii)

    # Assert
    assert "score" in analysis
    assert "classification" in analysis
    assert analysis['score'] < 0.5
    assert analysis['classification'] == "Não Recomendado"
