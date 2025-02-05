from converters.currency_converter import CurrencyConverter
from data_processing.data_processor import DataProcessor
from file_operations.data_loader import DataLoader
from file_operations.result_saver import ResultSaver
from config.config import Config
import os


def main():
    """Main function to load data, process it, and save the results."""
    data = DataLoader.load_csv(os.path.join(Config.INPUT_FILE_FOLDER, Config.DATA))
    currencies = DataLoader.load_csv(
        os.path.join(Config.INPUT_FILE_FOLDER, Config.CURRENCIES)
    )
    matchings = DataLoader.load_csv(
        os.path.join(Config.INPUT_FILE_FOLDER, Config.MATCHINGS)
    )

    currency_converter = CurrencyConverter(currencies)

    for row in data:
        row["price_pln"] = currency_converter.convert_to_pln(
            float(row["price"]), row["currency"]
        )

    results = DataProcessor.process_data(data, matchings)
    ResultSaver.save_results(
        results, (os.path.join(Config.OUTPUT_FILE_FOLDER, Config.TOP_PRODUCTS))
    )


if __name__ == "__main__":
    main()
