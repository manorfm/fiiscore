import re

class Indicator:
    def __init__(self, name, value):
        self.name = name
        self.value = self._to_float(value)

    def _expand_number(self, number, original_string):
        """Expands numbers with suffixes like B, M, K."""
        original_string = str(original_string).upper()
        if "B" in original_string:
            return number * 10**9
        if "M" in original_string:
            return number * 10**6
        if "K" in original_string:
            return number * 10**3
        return number

    def _to_float(self, value):
        """
        Converts a string value from the scraper to a clean float.
        Handles currency, percentages, and large number suffixes (B, M, K).
        Returns 0.0 for non-numeric values.
        """
        if isinstance(value, (int, float)):
            return float(value)

        original_value = str(value).strip()
        if not original_value:
            return 0.0

        is_percentage = "%" in original_value

        # Remove currency symbols and suffixes for cleaning
        cleaned_str = re.sub(r"[R$BKMBKM%]", "", original_value).strip()

        # Intelligent cleaning for pt-BR format (e.g., "1.234,56")
        if ',' in cleaned_str and '.' in cleaned_str:
            cleaned_str = cleaned_str.replace('.', '').replace(',', '.')
        else:
            cleaned_str = cleaned_str.replace(',', '.')

        try:
            number = float(cleaned_str)
        except (ValueError, TypeError):
            return 0.0

        number = self._expand_number(number, original_value)

        if is_percentage:
            number /= 100

        return number
        
    def __str__(self):
        return f"{self.__class__.__name__}({self.name}={self.value})"
