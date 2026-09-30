from pathlib import Path
import os

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"
RESULTS_DIR = BASE_DIR / "results"

BUYER_CSV = DATA_DIR / "comprador.csv"
PRODUCTS_CSV = DATA_DIR / "produtos.csv"
LOG_FILE = RESULTS_DIR / "execution.log"

FAKE_NAME_URL = "https://www.fakenamegenerator.com/"
SAUCE_DEMO_URL = "https://www.saucedemo.com/"

SAUCE_USERNAME = os.getenv(
    "SAUCE_USERNAME",
    "standard_user"
)

SAUCE_PASSWORD = os.getenv(
    "SAUCE_PASSWORD",
    "secret_sauce"
)

WEB_HEADLESS = os.getenv(
    "WEB_HEADLESS",
    "false"
).lower() == "true"

WEB_TIMEOUT = int(
    os.getenv(
        "WEB_TIMEOUT",
        "15000"
    )
)

def ensure_directories():
    DATA_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    RESULTS_DIR.mkdir(
        parents=True,
        exist_ok=True
    )