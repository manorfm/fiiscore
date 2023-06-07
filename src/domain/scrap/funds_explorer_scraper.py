import requests
from bs4 import BeautifulSoup
from src.domain.scrap.model.indicator import Indicator
from src.domain.scrap.model.fii import FIIScrapped
from src.domain.scrap.fii_not_fount_exception import FIINotFoundException

class FundsExplorerScrapper:
    __base = "https://www.fundsexplorer.com.br/funds/"

    def __getValue(self, p):
        return p.get_text().strip()

    def __get_indicators(self, fii, page):
        main = page.find('div', id="indicators")

        if main is not None:
           return main.find_all("div", class_="indicators__box")

        raise FIINotFoundException(f"FII {fii} not found!")

    def __get_page(self, fii):
        url = self.__base + fii
        page = requests.get(url)
        return BeautifulSoup(page.content, "html.parser")

    def __get_price(self, page):
        div = page.find('div', {"class": "headerTicker__content__price"})
        return div.p

    def __extract_indicator(self, box):
        fields = box.find_all('p')
        name = self.__getValue(fields[0])
        value = self.__getValue(fields[1])
        return Indicator(name, value)

    def execute(self, fii):
        page = self.__get_page(fii)
        div_indicators = self.__get_indicators(fii, page)

        indicators: list[Indicator] = []
        for div_indicator in div_indicators:
            indicators.append(self.__extract_indicator(div_indicator))

        price_indicator = self.__get_price(page)
        price = self.__getValue(price_indicator)

        indicators.append(Indicator("Price", price))

        return FIIScrapped(fii, indicators).to_fii()