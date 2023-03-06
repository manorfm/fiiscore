from src.domain.model.indicator import Indicator
from decimal import Decimal 

def testValueWithDotShouldRemoveit():
    "should remove dot from the value"
    indicator = Indicator("test", "10.000")
    assert indicator.value == 10000

def testValueIndicatorShouldBeDecimal():
    "should the value be an decimal"
    indicator = Indicator("test", "10,0")
    assert indicator.value == 10

def testValueIndicatorWithMiStringToBeExpanded():
    "given value when have mi on it then should expanded to milion"
    indicator = Indicator("test", "10 mi")
    assert indicator.value == 10_000_000

def testValueIndicatorWithBiStringToBeExpanded():
    "given value when have bi on it then should expanded to bilion"
    indicator = Indicator("test", "10 bi")
    assert indicator.value == 10_000_000_000

def testValueIndicatorWithRealSymbolShouldBeRemoved():
    "given value when have R$ symbol then should be removed"
    indicator = Indicator("test", "R$ 10")
    assert indicator.value == 10

def testValueIndicatorWithPercentageSymbolShouldBeRemoved():
    "given value when have % symbol then should be removed"
    indicator = Indicator("test", "10 %")
    assert indicator.value == 10

def testValueIndicatorWithNumberThenShouldAccept():
    "given value when have % symbol then should be removed"
    indicator = Indicator("test", 10)
    assert indicator.value == 10