import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class DashboardPage(BasePage):
    links = Links()
    PAGE_URL = links.DASHBOARD_PAGE
    MY_INFO_BUTTON = (By.XPATH, '//span[text()="My Info"]')

    @allure.step('Click on "My Info" link')
    def click_my_info_link(self):
        """Нажатие на кнопку My info"""
        self.wait.until(EC.element_to_be_clickable(self.MY_INFO_BUTTON)).click()