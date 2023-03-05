class FII:
    def __init__(self, name, indicators):
        self.name = name
        self.indicators = indicators

    def __str__(self):
        return  str(self.__class__) + '\n'+ '\n'.join(('{} = {}'.format(item, self.__dict__[item]) for item in self.__dict__))
