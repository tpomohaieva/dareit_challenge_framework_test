import os
import unittest

from PIL import Image
from selenium import webdriver

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service


class TestDashboardPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(service=Service(executable_path=DRIVER_PATH))
        self.driver.get("https://scouts-test.futbolkolektyw.pl/en/players/add")
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    @classmethod
    def test_change_language(self): # ST06
        user_login = LoginPage(self.driver)
        user_login.type_in_email("user01@getnada.com")
        user_login.type_in_password("Test-1234")
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_the_page()
        self.driver.save_screenshot("C:/Users/tpomo/Documents/GitHub/challenge_1_pomohaieva/test_cases/screenshots/check_dashboard/before-lang-change.png")
        Image.open("C:/Users/tpomo/Documents/GitHub/challenge_1_pomohaieva/test_cases/screenshots/check_dashboard/before-lang-change.png").show()
        dashboard_page.click_on_change_language()
        dashboard_page.assert_element_text(self.driver, dashboard_page.language_select_xpath,
                                           dashboard_page.language_pl_selected_text)
        self.driver.save_screenshot("C:/Users/tpomo/Documents/GitHub/challenge_1_pomohaieva/test_cases/screenshots/check_dashboard/after-lang-change.png")
        Image.open("C:/Users/tpomo/Documents/GitHub/challenge_1_pomohaieva/test_cases/screenshots/check_dashboard/after-lang-change.png").show()

    @classmethod
    def tearDown(self):
        self.driver.quit()
