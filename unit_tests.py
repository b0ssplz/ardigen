import unittest
from typing import List, Dict
from data_loader import DataLoader
from currency_converter import CurrencyConverter
from data_processor import DataProcessor
from result_saver import ResultSaver


class TestDataLoader(unittest.TestCase):
    def test_load_csv(self):
        """Test loading CSV file into a list of dictionaries."""
        sample_data = [{'id': '1', 'price': '100', 'currency': 'USD', 'quantity': '2', 'matching_id': '1'}]
        self.assertIsInstance(sample_data, List)
        self.assertIsInstance(sample_data[0], Dict)


class TestCurrencyConverter(unittest.TestCase):
    def setUp(self):
        """Initialize test data."""
        currency_data = [{'currency': 'USD', 'ratio': '4.0'}, {'currency': 'EUR', 'ratio': '4.5'},
                         {'currency': 'PLN', 'ratio': '1'}]
        self.converter = CurrencyConverter(currency_data)

    def test_convert_to_pln(self):
        """Test currency conversion to PLN."""
        self.assertEqual(self.converter.convert_to_pln(10, 'USD'), 40.0)
        self.assertEqual(self.converter.convert_to_pln(10, 'EUR'), 45.0)
        self.assertEqual(self.converter.convert_to_pln(10, 'PLN'), 10.0)
        self.assertEqual(self.converter.convert_to_pln(10, 'GBP'), 10.0)  # Default case if currency not found


class TestDataProcessor(unittest.TestCase):
    def test_process_data(self):
        """Test processing of data with matching rules."""
        sample_data = [
            {'price_pln': 100, 'quantity': 2, 'matching_id': 1, 'currency': 'PLN'},
            {'price_pln': 300, 'quantity': 1, 'matching_id': 1, 'currency': 'PLN'},
            {'price_pln': 150, 'quantity': 2, 'matching_id': 2, 'currency': 'PLN'}
        ]
        matchings = [{'matching_id': '1', 'top_priced_count': '1'}, {'matching_id': '2', 'top_priced_count': '1'}]

        processed_data = DataProcessor.process_data(sample_data, matchings)

        self.assertEqual(len(processed_data), 2)
        self.assertEqual(processed_data[0], (1, 300, 300, 'PLN', 2))  # Top product only, ignoring others
        self.assertEqual(processed_data[1], (2, 300, 150, 'PLN', 0))  # Single product included


if __name__ == "__main__":
    unittest.main()
