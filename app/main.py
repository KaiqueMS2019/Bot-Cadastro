from infrastructure.csv_repository import CsvRepository
from web.identity_generator import IdentityGenerator
from web.extract_sauce_demo import SauceDemo
from desktop.fill_out_fakturama import Fakturama
from infrastructure.logger import setup_logger


def main():
    logger = setup_logger()

    logger.info("Processo iniciado")

    repository = CsvRepository()

    logger.info("Gerando comprador")

    identity = IdentityGenerator()

    try:
        identity.open()
        buyer = identity.generate()
        buyer_path = repository.save_buyer(buyer)

        logger.info(
            f"Comprador salvo em: {buyer_path}"
        )
    finally:
        identity.close()

    logger.info("Extraindo catálogo do SauceDemo")

    sauce = SauceDemo()

    try:
        sauce.open()
        sauce.login()
        products = sauce.get_products()
        products_path = repository.save_products(products)

        logger.info(
            f"Catálogo salvo em: {products_path}"
        )

        logger.info(
            f"Total de produtos extraídos: {len(products)}"
        )
    finally:
        sauce.close()

    logger.info("Iniciando automação do Fakturama")

    fakturama = Fakturama(
        r"C:\Program Files\Fakturama2\Fakturama.exe"
    )

    fakturama.open()

    fakturama.register_buyer(buyer)
    fakturama.screenshot_buyer()

    logger.info("Comprador cadastrado no Fakturama")

    fakturama.registers_products(products)
    fakturama.screenshot_products()
    logger.info("Produtos cadastrados no Fakturama")
    fakturama.close()
    logger.info("Processo finalizado com sucesso")


if __name__ == "__main__":
    main()