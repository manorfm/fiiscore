import pytest
from unittest.mock import patch, MagicMock
from src.domain.scrap.funds_explorer_scraper import FundsExplorerScrapper
from src.domain.scrap.fii_not_fount_exception import FIINotFoundException

@pytest.fixture
def mock_successful_response():
    """Provides a mock successful HTTP response that mimics the real site structure."""
    mock_response = MagicMock()
    mock_response.status_code = 200

    html_content = """
    <html>
        <body>
            <div id="indicators">
                <div class="indicators__box">
                    <p class="indicator-title">Dividend Yield</p>
                    <p class="indicator-value">0,94%</p>
                </div>
                <div class="indicators__box">
                    <p class="indicator-title">Último Rendimento</p>
                    <p class="indicator-value">R$ 0,74</p>
                </div>
                 <div class="indicators__box">
                    <p class="indicator-title">P/VP</p>
                    <p class="indicator-value">0,82</p>
                </div>
                <div class="indicators__box">
                    <p class="indicator-title">Liquidez Diária</p>
                    <p class="indicator-value">R$ 1.234.567,00</p>
                </div>
                <div class="indicators__box">
                    <p class="indicator-title">Vacância</p>
                    <p class="indicator-value">5,50%</p>
                </div>
                <div class="indicators__box">
                    <p class="indicator-title">Quantidade de ativos</p>
                    <p class="indicator-value">7</p>
                </div>
            </div>
            <div class="headerTicker__content__price">
                <p>R$ 79,50</p>
            </div>
        </body>
    </html>
    """
    mock_response.content = html_content.encode('utf-8')
    mock_response.text = html_content
    return mock_response

@patch('requests.get')
def test_scrape_fii_successfully(mock_get, mock_successful_response):
    """Should successfully scrape FII data when the response is valid."""
    # Arrange
    mock_get.return_value = mock_successful_response
    scraper = FundsExplorerScrapper()

    # Act
    fii = scraper.execute("hgre11")

    # Assert
    assert fii.name == "hgre11"
    assert fii.price == pytest.approx(79.5)
    assert fii.lastIncome == pytest.approx(0.74)
    assert fii.dividendYield == pytest.approx(0.0094)
    assert fii.pvp == pytest.approx(0.82)
    assert fii.daily_liquidity == pytest.approx(1234567.0)
    assert fii.vacancy == pytest.approx(0.055)
    assert fii.asset_amount == 7
