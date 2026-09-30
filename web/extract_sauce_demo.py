from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from domain.models import Product


class SauceDemo:
    URL = "https://www.saucedemo.com/"
    USERNAME = "standard_user"
    PASSWORD = "secret_sauce"

    def __init__(self):
        self.driver = None
        self.wait = None

    def open(self):
        options = Options()
        options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 20)

        self.driver.get(self.URL)

    def login(self):
        username = self.wait.until(
            EC.visibility_of_element_located(
                (By.ID, "user-name")
            )
        )

        password = self.driver.find_element(
            By.ID,
            "password"
        )

        login_button = self.driver.find_element(
            By.ID,
            "login-button"
        )

        username.send_keys(self.USERNAME)
        password.send_keys(self.PASSWORD)
        login_button.click()

        self.wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "inventory_list")
            )
        )

    def get_products(self):
        elements = self.driver.find_elements(
            By.CSS_SELECTOR,
            ".inventory_item"
        )

        products = []

        for number, element in enumerate(elements, start=1):
            name = element.find_element(
                By.CSS_SELECTOR,
                ".inventory_item_name"
            ).text.strip()

            description = element.find_element(
                By.CSS_SELECTOR,
                ".inventory_item_desc"
            ).text.strip()

            price_text = element.find_element(
                By.CSS_SELECTOR,
                ".inventory_item_price"
            ).text.strip()

            price = float(
                price_text.replace("$", "").replace(",", ".")
            )

            products.append(
                Product(
                    number=number,
                    name=name,
                    description=description,
                    price=price
                )
            )

        return products

    def close(self):
        if self.driver:
            self.driver.quit()


if __name__ == "__main__":
    sauce = SauceDemo()

    try:
        sauce.open()
        sauce.login()

        products = sauce.get_products()

        print(f"Produtos encontrados: {len(products)}")

        for product in products:
            print(
                f"{product.number}. "
                f"{product.name} - "
                f"${product.price:.2f}"
            )
    finally:
        sauce.close()