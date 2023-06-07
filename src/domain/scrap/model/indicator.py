from decimal import Decimal
import re

class Indicator:
    def __init__(self, name, value):
        self.name = name
        self.value = self.__toDecimal(value)

    def __numberExpander(self, number, original):
        if "B" in original:
            return number * 10**9
        elif "M" in original:
            return number * 10**6
        elif "K" in original:
            return number * 10**3
        return number

    def __toDecimal(self, value):
        if isinstance(value, int | float):
            return value
        decimalStr = re.sub(r"[R$|%|B|M|K|\.]", "", value).replace(',', '.')
        return self.__numberExpander(Decimal(decimalStr), value)
        
    def __str__(self):
        return  str(self.__class__) + '\n'+ '\n'.join(('{} = {}'.format(item, self.__dict__[item]) for item in self.__dict__))
