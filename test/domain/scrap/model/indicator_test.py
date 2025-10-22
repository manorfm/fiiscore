import pytest
from src.domain.scrap.model.indicator import Indicator

@pytest.mark.parametrize("input_value, expected_float", [
    ("R$ 1.234,56", 1234.56),
    ("10,5%", 0.105),
    ("1.2M", 1200000.0),
    ("5B", 5000000000.0),
    (1500, 1500.0),
    ("N/A", 0.0),
    ("", 0.0),
])
def test_indicator_value_conversion(input_value, expected_float):
    """
    Should convert various string formats to the correct float value.
    """
    indicator = Indicator("test_indicator", input_value)
    assert indicator.value == pytest.approx(expected_float)

def test_indicator_with_empty_value():
    """Should handle empty or whitespace-only values gracefully."""
    indicator = Indicator("empty_indicator", "  ")
    assert indicator.value == 0.0

def test_indicator_string_representation():
    """Should have a clear string representation."""
    indicator = Indicator("pvp", 1.05)
    assert str(indicator) == "Indicator(pvp=1.05)"
