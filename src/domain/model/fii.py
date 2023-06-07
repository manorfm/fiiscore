from decimal import Decimal
class FII:
    def __init__(self, name, price, lastIncome, dividendYield, pvp, forecast = 0.0):
        self.name = name
        self.price = price
        self.lastIncome = lastIncome
        self.dividendYield = dividendYield
        self.pvp = pvp

        if (forecast > 0.0):
            self.qnt: int = forecast//price
            self.forecast = "R$ {:.2f}".format( self.qnt * lastIncome ) 


    def __str__(self):
        return  str(self.__class__) + '\n'+ '\n'.join(('{} = {}'.format(item, self.__dict__[item]) for item in self.__dict__))

    def score(self) -> float:
        score = ((self.lastIncome * self.dividendYield) / ((self.price * 2) * (self.pvp * 6))) / (2 * 6)
        return round(score* 1000, 2)

class FIIBuilder:
    def __init__(self, name, forecast: float):
        self.name = name
        self.forecast = forecast
        self.lastIncome: float = 0.0
        self.dividendYield: float = 0.0
        self.price: float = 0.0
        self.pvp: float = 0.0

    def build(self)-> FII:
        return FII(self.name, self.price, self.lastIncome, self.dividendYield, self.pvp, self.forecast)

