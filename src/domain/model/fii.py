class FII:
    def __init__(self, name, price, lastIncome, dividendYield, pvp):
        self.name = name
        self.price = price
        self.lastIncome = lastIncome
        self.dividendYield = dividendYield
        self.pvp = pvp

    def __str__(self):
        return  str(self.__class__) + '\n'+ '\n'.join(('{} = {}'.format(item, self.__dict__[item]) for item in self.__dict__))
    
    def score(self) -> float:
        score = (self.lastIncome * self.dividendYield) / (self.price * self.pvp)
        return round(score* 1000, 2)
    
class FIIBuilder:
    def __init__(self, name):
        self.name = name
        self.lastIncome: float = 0.0
        self.dividendYield: float = 0.0
        self.price: float = 0.0
        self.pvp: float = 0.0


    def build(self)-> FII:
        return FII(self.name, self.price, self.lastIncome, self.dividendYield, self.pvp)

