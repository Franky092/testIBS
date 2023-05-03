import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import json
from pages.web_pages.home_page import HomePage

@allure.label("owner", "admin")
@allure.title("Проверка результата запроса list user")
@allure.link("https://reqres.in/")
def test_listuser(get_webdriver):
    with allure.step("Загружаем главную страницу"):
        home_page = HomePage(get_webdriver)
        home_page.open()
        pass
    with allure.step("Нажимаем на list users"):
        # get_webdriver.execute_script("window.scrollTo(0, 1000)")
        WebDriverWait(get_webdriver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.endpoints ul li:nth-of-type(1)"))).click()
        time.sleep(1)

        pass
    with allure.step("Получаем статус код с сайта"):
    # get_webdriver.execute_script("window.scrollTo(0, 1000)")
        statuscode = int(WebDriverWait(get_webdriver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span.response-code"))).text)
        time.sleep(1)
        pass
    with allure.step("Отправляем апи запрос"):
        from tests.api_tests.test_listuser import test_get_users
        apistatuscode = test_get_users(page=1, per_page=6, expected_status=200)[0]
    pass
    with allure.step("Проверяем статус код со страницы и с АПИ"):
        assert statuscode == apistatuscode
    pass
    with allure.step("Получаем тело запроса с сайта"):
        # get_webdriver.execute_script("window.scrollTo(0, 1000)")
        webbodyresponse = WebDriverWait(get_webdriver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "pre[data-key*='output-response']"))).text
        webbodyresponse = json.loads(webbodyresponse)
        time.sleep(1)

    pass
    with allure.step("Отправляем апи запрос и возвращаем тело"):
        from tests.api_tests.test_listuser import test_get_users
        apibodyresponce = test_get_users(page=2, per_page=6, expected_status=200)[1]
        apibodyresponce = json.loads(apibodyresponce)
    pass
    with allure.step("Проверяем статус код со страницы и с АПИ"):
        assert webbodyresponse == apibodyresponce
    pass
pass

