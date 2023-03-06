import requests
from bs4 import BeautifulSoup
from src.domain.model.indicator import Indicator
from src.domain.model.fii import FII
from src.domain.scrap.fii_not_fount_exception import FIINotFoundException

class FundsExplorerScrapper:
    __base = "https://www.fundsexplorer.com.br/funds/"

    def __getValue(self, div_indicator, class_):
        return div_indicator.find("span", class_=class_).get_text().strip()

    def __navigate(self, fii):
        url = self.__base + fii
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        main = soup.find('div', id="main-indicators-carousel")

        if main is not None:
           return main.find_all("div", class_="carousel-cell")
        raise FIINotFoundException(f"FII {fii} not found!")

    def execute(self, fii):
        results = self.__navigate(fii)

        indicators: list[Indicator] = []
        for div_indicator in results:
            name = self.__getValue(div_indicator, "indicator-title")
            value = self.__getValue(div_indicator, "indicator-value")
            indicators.append(Indicator(name, value))

        return FII(fii, indicators)