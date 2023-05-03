class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.url)

    def close(self):
        self.driver.quit()


class HomePage(BasePage):
    url = "https://reqres.in"



