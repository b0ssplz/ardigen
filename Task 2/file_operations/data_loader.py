import csv
from typing import List, Dict


class DataLoader:
    """Handles loading of CSV files."""

    @staticmethod
    def load_csv(filename: str) -> List[Dict[str, str]]:
        """Loads data from a CSV file and returns it as a list of dictionaries."""
        with open(filename, mode='r', encoding='utf-8') as file:
            return list(csv.DictReader(file))
