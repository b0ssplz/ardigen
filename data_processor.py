from typing import List, Dict, Tuple


class DataProcessor:
    """Processes product data to select top-priced items per matching_id and aggregates results."""

    @staticmethod
    def process_data(data: List[Dict[str, str]], matchings: List[Dict[str, str]]) -> \
            List[Tuple[int, float, float, str, int]]:
        """Processes product data to determine top-priced products per matching_id."""
        results = []
        grouped_data: Dict[int, List[Dict[str, str]]] = {}

        for row in data:
            row['price_pln'] = float(row['price_pln'])
            row['quantity'] = int(row['quantity'])
            row['matching_id'] = int(row['matching_id'])
            grouped_data.setdefault(row['matching_id'], []).append(row)

        for match in matchings:
            matching_id = int(match['matching_id'])
            top_count = int(match['top_priced_count'])

            products = sorted(grouped_data.get(matching_id, []), key=lambda x: x['price_pln'] * x['quantity'],
                              reverse=True)
            top_products = products[:top_count]
            ignored_products_count = max(0, len(products) - len(top_products))

            total_pr = sum(p['price_pln'] * p['quantity'] for p in top_products)
            avg_price = sum(p['price_pln'] for p in top_products) / len(top_products) if top_products else 0
            currency = top_products[0]['currency'] if top_products else "PLN"

            results.append((matching_id, total_pr, avg_price, currency, ignored_products_count))

        return results
