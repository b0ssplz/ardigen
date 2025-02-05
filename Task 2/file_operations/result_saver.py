import csv
from typing import List, Tuple


class ResultSaver:
    """Handles saving the processed results into a CSV file."""

    @staticmethod
    def save_results(results: List[Tuple[int, float, float, str, int]], filename: str) -> None:
        """Saves the processed results into a CSV file."""
        headers = ["matching_id", "total_pr", "avg_price", "currency", "ignored_products_count"]
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(results)
