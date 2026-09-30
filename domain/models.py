from dataclasses import dataclass

@dataclass(frozen=True)
class Buyer:
    first_name: str
    last_name: str
    cep: str


@dataclass(frozen=True)
class Product:
    number: int
    name: str
    description: str
    price: float