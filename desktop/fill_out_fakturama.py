from pathlib import Path
from botcity.core import DesktopBot
from infrastructure.logger import setup_logger

class Fakturama:
    def __init__(self, executable_path):
        self.executable_path = Path(executable_path)
        self.bot = DesktopBot()
        self.assets = Path("desktop/assets")
        self.logger = setup_logger()

        self.bot.add_image(
            "New_contact",
            str(self.assets / "New_contact.png")
        )

        self.bot.add_image(
            "first_name",
            str(self.assets / "first_name.png")
        )

        self.bot.add_image(
            "district",
            str(self.assets / "district.png")
        )

        self.bot.add_image(
            "save_fakturama",
            str(self.assets / "save_fakturama.png")
        )
        self.bot.add_image(
            "New_product",
            str(self.assets / "New_product.png")
        )
        self.bot.add_image(
            "number_product",
            str(self.assets / "number_product.png")
        )
        self.bot.add_image(
            "description_product",
            str(self.assets / "description_product.png")
        )

    def open(self):
        if not self.executable_path.exists():
            raise FileNotFoundError(
                f"Fakturama não encontrado: {self.executable_path}"
            )

        self.logger.info("Abrindo Fakturama")
        self.bot.execute(str(self.executable_path))
        self.bot.sleep(7000)
        self.logger.info("Fakturama aberto")

    def find_image(self, image_name, waiting_time=10000):
        element = self.bot.find(
            label=image_name,
            waiting_time=waiting_time
        )

        if not element:
            raise RuntimeError(
                f"Imagem não encontrada na tela: {image_name}"
            )

        return element

    def click_image(self, image_name, waiting_time=10000):
        self.find_image(
            image_name,
            waiting_time
        )

        self.bot.click()

    def register_buyer(self, buyer):
        self.logger.info(
            f"Cadastrando comprador: "
            f"{buyer.first_name} {buyer.last_name}"
        )

        self.click_image(
            "New_contact",
            waiting_time=15000
        )

        self.click_image(
            "first_name",
            waiting_time=10000
        )

        self.bot.type_key(buyer.first_name)
        self.bot.tab()
        self.bot.type_key(buyer.last_name)
        self.bot.tab()

        self.click_image(
            "district",
            waiting_time=10000
        )

        self.bot.tab()
        self.bot.type_key(buyer.cep)
        self.click_image(
            "save_fakturama",
            waiting_time=10000
        )

        self.bot.sleep(1500)
        self.logger.info("Comprador Cadastrado")

    def registers_products(self, products):
        self.logger.info(
            f"Iniciando cadastro de {len(products)} produtos"
        )
        for product in products:
            self.logger.info(
                f"Iniciando cadastro de {len(products)} produtos"
            )
            self.click_image(
                "New_product",
                waiting_time=15000
            )
            self.click_image(
                "number_product",
                waiting_time=10000
            )

            self.bot.type_key(str(product.number))
            self.bot.tab()
            self.bot.type_key(product.name)
            self.bot.tab()
            self.click_image(
                "description_product",
                waiting_time=10000
            )
            self.bot.type_key(product.description)
            self.bot.tab()
            self.bot.control_a()
            self.bot.backspace()
            self.bot.type_key(str(product.price))
            self.click_image(
                "save_fakturama",
                waiting_time=10000
            )
            self.logger.info(
                f"Produto {product.number} cadastrado com sucesso"
            )
        self.logger.info("Cadastro de produtos finalizado")

    def screenshot(self, path):
        Path(path).parent.mkdir(
            parents=True,
            exist_ok=True
        )

        self.bot.save_screenshot(str(path))

    def screenshot_buyer(self):
        self.screenshot(
            "results/buyer_registered.png"
        )

    def screenshot_products(self):
        self.screenshot(
            "results/products_registered.png"
        )

    def close(self):
        self.bot.alt_f4()
        self.bot.sleep(2000)
