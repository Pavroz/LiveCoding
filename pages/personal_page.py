import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class PersonalPage(BasePage):
    links = Links()
    PAGE_URL = links.PERSONAL_PAGE
    FIRST_NAME_FIELD = ('css', 'input[name="firstName"]') # Поле ввода имени
    SAVE_BUTTON = ('xpath', '(//button[@type="submit"])[1]') # Кнопка сохранения изменений

    def change_name(self, new_name):
        """Очистка поля ввода имени и ввод нового имени"""
        with allure.step(f'Change name on "{new_name}"'):
            first_name_field = self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME_FIELD))
            first_name_field.clear()
            assert first_name_field.get_attribute('value') == '', 'There is text'
            first_name_field.send_keys(new_name)
            self.name = new_name

    @allure.step('Save changes')
    def save_changes(self):
        """Сохранение изменений"""
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()

    @allure.step('Changes has been saved successfully')
    def is_changes_saved(self):
        """Проверка, что имя поменялось на то, которое вводили"""
        self.wait.until(EC.text_to_be_present_in_element_value(self.SAVE_BUTTON, self.name))