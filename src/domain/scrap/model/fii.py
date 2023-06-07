from src.domain.model.fii import FIIBuilder
class FIIScrapped:
    def __init__(self, name, indicators, forecast: float = 0.0):
        self.name = name
        self.indicators = indicators
        self.forecast = forecast

    def __str__(self):
        return  str(self.__class__) + '\n'+ '\n'.join(('{} = {}'.format(item, self.__dict__[item]) for item in self.__dict__))

    def to_fii(self):
        builder = FIIBuilder(self.name, self.forecast)

        for indicator in self.indicators:
            if indicator.name == "Dividend Yield":
                builder.dividendYield = indicator.value
            elif indicator.name == "Último Rendimento":
                builder.lastIncome = indicator.value
            elif indicator.name == "Price":
                builder.price = indicator.value
            elif indicator.name == "P/VP":
                builder.pvp = indicator.value
        
        return builder.build()
    


