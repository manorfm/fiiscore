from decimal import Decimal
class FII:
    def __init__(self, name, price, lastIncome, dividendYield, pvp, url, forecast: float = 0.0,
                 daily_liquidity: float = 0.0, vacancy: float = 0.0, asset_amount: int = 0):
        self.name = name
        self.price = float(price)
        self.lastIncome = float(lastIncome)
        self.dividendYield = float(dividendYield)
        self.pvp = float(pvp)
        self.url = url
        self.daily_liquidity = daily_liquidity
        self.vacancy = vacancy
        self.asset_amount = asset_amount


        if (forecast > 0.0):
            self.qnt: int = forecast // self.price
            self.forecast = "R$ {:.2f}".format( self.qnt * self.lastIncome ) 


    def __str__(self):
        return  str(self.__class__) + '\n'+ '\n'.join(('{} = {}'.format(item, self.__dict__[item]) for item in self.__dict__))

class FIIBuilder:
    def __init__(self, name, url, forecast: float):
        self.name = name
        self.forecast = forecast
        self.lastIncome: float = 0.0
        self.dividendYield: float = 0.0
        self.price: float = 0.0
        self.pvp: float = 0.0
        self.url = url
        self.daily_liquidity: float = 0.0
        self.vacancy: float = 0.0
        self.asset_amount: int = 0

    def build(self)-> FII:
        return FII(self.name, self.price, self.lastIncome, self.dividendYield, self.pvp, self.url, self.forecast,
                   self.daily_liquidity, self.vacancy, self.asset_amount)

