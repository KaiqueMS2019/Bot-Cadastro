import csv
from pathlib import Path

from domain.models import Buyer, Product


class CsvRepository:
    def __init__(self, data_dir="data"):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)

    def save_buyer(self, buyer: Buyer):
        path = self.data_dir / "buyer.csv"

        with path.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["first_name", "last_name", "CEP"]
            )

            writer.writeheader()
            writer.writerow({
                "first_name": buyer.first_name,
                "last_name": buyer.last_name,
                "CEP": buyer.cep
            })

        return path

    def save_products(self, products: list[Product]):
        path = self.data_dir / "products.csv"

        with path.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=[
                    "number",
                    "name",
                    "description",
                    "price"
                ]
            )

            writer.writeheader()

            for product in products:
                writer.writerow({
                    "number": product.number,
                    "name": product.name,
                    "description": product.description,
                    "price": f"{product.price:.2f}"
                })

        return path

    def load_buyer(self):
        path = self.data_dir / "buyer.csv"

        with path.open(
                "r",
                newline="",
                encoding="utf-8"
        ) as file:
            row = next(csv.DictReader(file))

        return Buyer(
            first_name=row["first_name"],
            last_name=row["last_name"],
            cep=row["CEP"]
        )

    def load_products(self):
        path = self.data_dir / "products.csv"

        with path.open(
                "r",
                newline="",
                encoding="utf-8"
        ) as file:
            rows = csv.DictReader(file)

            return [
                Product(
                    number=int(row["number"]),
                    name=row["name"],
                    description=row["description"],
                    price=float(row["price"])
                )
                for row in rows
            ]