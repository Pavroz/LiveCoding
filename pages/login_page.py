import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    links = Links()
    PAGE_URL = links.LOGIN_PAGE
    USERNAME_FIELD = (By.CSS_SELECTOR, 'input[name="username"]')
    PASSWORD_FIELD = (By.CSS_SELECTOR, 'input[name="password"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')

    @allure.step('Enter login')
    def enter_login(self, login):
        """Ввод логина в поле ввода"""
        self.wait.until(EC.element_to_be_clickable(self.USERNAME_FIELD)).send_keys(login)

    @allure.step('Enter password')
    def enter_password(self, password):
        """Ввод пароля в поле ввода"""
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(password)

    @allure.step('Click submit button')
    def click_submit_button(self):
        """Нажатие на кнопку входа"""
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()

    @allure.step('Authorization is done!')
    def auth(self, login, password):
        """Функция авторизации"""
        self.enter_login(login)
        self.enter_password(password)
        self.click_submit_button()