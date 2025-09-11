import time

import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class PersonalPage(BasePage):
    links = Links()
    PAGE_URL = links.PERSONAL_PAGE
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, 'input[name="firstName"]') # Поле ввода имени
    SAVE_BUTTON = (By.XPATH, '(//button[@type="submit"])[1]') # Кнопка сохранения изменений
    SPINNER = (By.CSS_SELECTOR, 'div.oxd-loading-spinner') # Спиннер после сохранения данных

    def change_name(self, new_name):
        """Очистка поля ввода имени и ввод нового имени"""
        with allure.step(f'Change name on "{new_name}"'):
            first_name_field = self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME_FIELD))
            # time.sleep(5)
            # first_name_field.clear()
            # # self.driver.find_element(*self.FIRST_NAME_FIELD).clear()
            first_name_field.send_keys(Keys.CONTROL + "a")
            first_name_field.send_keys(Keys.BACKSPACE)
            first_name_field.send_keys(new_name)
            self.name = new_name

    @allure.step('Save changes')
    def save_changes(self):
        """Сохранение изменений"""
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()

    @allure.step('Changes has been saved successfully')
    def is_changes_saved(self):
        """Проверка, что имя поменялось на то, которое вводили"""
        self.wait.until(EC.invisibility_of_element_located(self.SPINNER)) # Ожидание, пока пропадет спиннер
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME_FIELD)) # Ждем появление поля ввода
        self.wait.until(EC.text_to_be_present_in_element_value(self.FIRST_NAME_FIELD, self.name)) # Сравнение текста

