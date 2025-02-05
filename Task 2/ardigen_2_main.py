import csv
from typing import List, Dict, Tuple
from file_operations.data_loader import DataLoader
from converters.currency_converter import CurrencyConverter
from data_processing.data_processor import DataProcessor
from file_operations.result_saver import ResultSaver


def main():
    """Main function to load data, process it, and save the results."""
    data = DataLoader.load_csv("data.csv")
    currencies = DataLoader.load_csv("currencies.csv")
    matchings = DataLoader.load_csv("matchings.csv")

    currency_converter = CurrencyConverter(currencies)

    for row in data:
        row['price_pln'] = currency_converter.convert_to_pln(float(row['price']), row['currency'])

    results = DataProcessor.process_data(data, matchings)
    ResultSaver.save_results(results, "top_products.csv")


if __name__ == "__main__":
    main()
