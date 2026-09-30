import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from domain.models import Buyer


class IdentityGenerator:
    URL = "https://pt.fakenamegenerator.com/gen-random-br-br.php"

    def __init__(self):
        self.driver = None
        self.wait = None

    def open(self):
        options = Options()
        options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.get(self.URL)

    def generate(self) -> Buyer:
        identity = self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".info")
            )
        )

        name = identity.find_element(
            By.CSS_SELECTOR, "h3"
        ).text.strip()

        address_lines = identity.find_element(
            By.CSS_SELECTOR, ".adr"
        ).text.strip().splitlines()

        cep = self._extract_cep(address_lines)

        first_name, last_name = self._split_name(name)

        return Buyer(
            first_name=first_name,
            last_name=last_name,
            cep=cep
        )

    @staticmethod
    def _extract_cep(address_lines):
        for line in address_lines:
            match = re.search(r"\b\d{5}-\d{3}\b", line)

            if match:
                return match.group()

        raise ValueError("CEP não encontrado na identidade gerada.")

    @staticmethod
    def _split_name(full_name):
        parts = full_name.split()

        if len(parts) < 2:
            raise ValueError("Nome completo inválido.")

        return parts[0], parts[-1]

    def close(self):
        if self.driver:
            self.driver.quit()


if __name__ == "__main__":
    generator = IdentityGenerator()

    try:
        generator.open()
        buyer = generator.generate()

        print(f"Nome: {buyer.first_name}")
        print(f"Sobrenome: {buyer.last_name}")
        print(f"CEP: {buyer.cep}")
    finally:
        generator.close()