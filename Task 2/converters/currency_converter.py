from typing import List, Dict


class CurrencyConverter:
    """Handles currency conversion based on provided exchange rates."""

    def __init__(self, currency_data: List[Dict[str, str]]):
        """Initializes the converter with a dictionary of currency exchange rates."""
        self.currency_rates = self.parse_currencies(currency_data)

    def convert_to_pln(self, price: float, currency: str) -> float:
        """Converts a given price from a specified currency to PLN."""
        return price * self.currency_rates.get(currency, 1)

    @staticmethod
    def parse_currencies(currency_data: List[Dict[str, str]]) -> Dict[str, float]:
        """Parses currency exchange rates from raw data."""
        return {row['currency']: float(row['ratio']) for row in currency_data}
