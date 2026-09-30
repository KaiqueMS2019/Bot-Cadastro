from domain.models import Buyer, Product
from infrastructure.csv_repository import CsvRepository


def test_save_buyer(tmp_path):
    repository = CsvRepository(tmp_path)

    buyer = Buyer(
        first_name="Joao",
        last_name="Silva",
        cep="12345-678"
    )

    path = repository.save_buyer(buyer)

    assert path.exists()

    content = path.read_text(encoding="utf-8")

    assert "Joao" in content
    assert "Silva" in content
    assert "12345-678" in content


def test_save_products(tmp_path):
    repository = CsvRepository(tmp_path)

    products = [
        Product(
            number=1,
            name="Produto 1",
            description="Descricao",
            price=29.99
        )
    ]

    path = repository.save_products(products)

    assert path.exists()

    content = path.read_text(encoding="utf-8")

    assert "Produto 1" in content
    assert "29.99" in content