import requests
from bs4 import BeautifulSoup
from src.domain.scrap.model.indicator import Indicator
from src.domain.scrap.model.fii import FIIScrapped
from src.domain.scrap.fii_not_fount_exception import FIINotFoundException

class FundsExplorerScrapper:
    __base = "https://www.fundsexplorer.com.br/funds/"

    def __getValue(self, div_indicator, class_):
        return div_indicator.find("span", class_=class_).get_text().strip()

    def __get_indicators(self, fii, page):
        main = page.find('div', id="main-indicators-carousel")

        if main is not None:
           return main.find_all("div", class_="carousel-cell")

        raise FIINotFoundException(f"FII {fii} not found!")

    def __get_page(self, fii):
        url = self.__base + fii
        page = requests.get(url)
        return BeautifulSoup(page.content, "html.parser")

    def __get_price(self, page):
        return page.find('div', id="stock-price")

    def execute(self, fii):
        page = self.__get_page(fii)
        div_indicators = self.__get_indicators(fii, page)

        indicators: list[Indicator] = []
        for div_indicator in div_indicators:
            name = self.__getValue(div_indicator, "indicator-title")
            value = self.__getValue(div_indicator, "indicator-value")
            indicators.append(Indicator(name, value))

        price_indicator = self.__get_price(page)
        price = self.__getValue(price_indicator, "price")

        indicators.append(Indicator("Price", price))

        return FIIScrapped(fii, indicators).to_fii()