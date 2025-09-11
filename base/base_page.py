import allure
from config.links import Links
from allure_commons.types import AttachmentType # для прикрепления каких-то файлов разного формата
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    links = Links()
    PAGE_URL = links.HOST
    def __init__(self, driver):
        """Принимает готовый драйвер от фикстуры, сохраняет в self.driver
        для использования в методах страницы (поиск элементов, ожидания)."""
        self.driver = driver # Сохраняет ссылку на драйвер из фикстуры для работы с элементами страницы
        self.wait = WebDriverWait(driver, 10, poll_frequency=1) # Инициализирует ожидание на основе драйвера

    def open(self):
        """Открытие браузера"""
        with allure.step(f'Open {self.PAGE_URL} page'):
            self.driver.get(self.PAGE_URL)

    def is_opened(self):
        """Проверка, что страница открылась"""
        with allure.step(f'Page {self.PAGE_URL} is opened'):
            self.wait.until(EC.url_to_be(self.PAGE_URL))

    def make_screenshot(self, screenshot_name):
        """Действие скриншота"""
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG
        )
