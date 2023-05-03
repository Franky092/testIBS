import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType


@pytest.fixture(scope='function')
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')  # Use headless if you do not need a browser UI
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")
    options.add_argument("disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--headless")
    return options


@pytest.fixture(scope="function")
def get_webdriver(get_chrome_options):
    print("\nstart browser for test..")
    driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()), chrome_options=get_chrome_options)
    yield driver
    print("\nquit browser..")
    driver.quit()


@pytest.fixture(scope="function")
def base_url():
    return "https://reqres.in/api"

@pytest.fixture(scope="function")
def base_url_web():
    return "https://reqres.in"