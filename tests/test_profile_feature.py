import random
import allure
import pytest
from base.base_test import BaseTest

@allure.feature('Profile Functionality')
class TestProfileFeature(BaseTest):

    @allure.title('Change profile name')
    @allure.severity('Critical')
    @pytest.mark.smoke
    def test_change_profile_name(self):
        """Тест смены имени"""
        self.login_page.open()
        self.login_page.auth(self.data.LOGIN, self.data.PASSWORD)
        self.dashboard_page.open()
        self.dashboard_page.is_opened()
        self.personal_page.open()
        self.personal_page.is_opened()
        self.personal_page.change_name(f'Test {random.randint(1, 100)}')
        self.personal_page.save_changes()
        self.personal_page.is_changes_saved()
        self.personal_page.make_screenshot('Success')