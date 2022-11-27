import os
import unittest
from selenium import webdriver

from pages.addPlayer_page import AddPlayerPage
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service
from PIL import Image


class TestAddPlayerPage(unittest.TestCase):
    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(service=Service(executable_path=DRIVER_PATH))
        self.driver.get("https://scouts-test.futbolkolektyw.pl/en/players/add")
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    @classmethod
    def test_add_player_with_valid_data(self):  # ST07
        user_login = LoginPage(self.driver)
        user_login.type_in_email("user01@getnada.com")
        user_login.type_in_password("Test-1234")
        user_login.click_on_the_sign_in_button()
        dashboard = Dashboard(self.driver)
        dashboard.click_on_add_player()
        add_player = AddPlayerPage(self.driver)
        add_player.title_of_the_page()
        self.driver.save_screenshot("C:/Users/tpomo/Documents/GitHub/challenge_1_pomohaieva/test_cases/screenshots/add_player/add-player.png")
        Image.open("C:/Users/tpomo/Documents/GitHub/challenge_1_pomohaieva/test_cases/screenshots/add_player/add-player.png").show()
        add_player.type_in_name("Test")
        add_player.type_in_surname("Testowski")
        add_player.type_in_age("01/01/1990")
        add_player.type_in_main_position("Forward")
        add_player.click_on_the_submit_button()
        add_player.player_added_title_of_the_page()
        add_player.assert_element_text(self.driver, add_player.add_player_form_title_xpath,
                                       add_player.player_added_form_title_text)
        self.driver.save_screenshot("C:/Users/tpomo/Documents/GitHub/challenge_1_pomohaieva/test_cases/screenshots/add_player/player-added.png")
        Image.open("C:/Users/tpomo/Documents/GitHub/challenge_1_pomohaieva/test_cases/screenshots/add_player/player-added.png").show()

    @classmethod
    def test_add_player_with_missing_required_data(self):  # ST08
        user_login = LoginPage(self.driver)
        user_login.type_in_email("user01@getnada.com")
        user_login.type_in_password("Test-1234")
        user_login.click_on_the_sign_in_button()
        dashboard = Dashboard(self.driver)
        dashboard.click_on_add_player()
        add_player = AddPlayerPage(self.driver)
        add_player.title_of_the_page()
        add_player.click_on_the_name_field()
        add_player.click_on_the_submit_button()
        add_player.show_name_required_error()
        self.driver.save_screenshot("C:/Users/tpomo/Documents/GitHub/challenge_1_pomohaieva/test_cases/screenshots/add_player/validation-error.png")
        Image.open("C:/Users/tpomo/Documents/GitHub/challenge_1_pomohaieva/test_cases/screenshots/add_player/validation-error.png").show()

    @classmethod
    def test_clear_date_on_add_player_form(self):  # ST09
        user_login = LoginPage(self.driver)
        user_login.type_in_email("user01@getnada.com")
        user_login.type_in_password("Test-1234")
        user_login.click_on_the_sign_in_button()
        dashboard = Dashboard(self.driver)
        dashboard.click_on_add_player()
        add_player = AddPlayerPage(self.driver)
        add_player.title_of_the_page()
        add_player.type_in_name("Test")
        add_player.type_in_surname("Testowski")
        add_player.type_in_phone("+48123456789")
        add_player.type_in_age("01/01/1990")
        add_player.type_in_main_position("Forward")
        self.driver.save_screenshot("C:/Users/tpomo/Documents/GitHub/challenge_1_pomohaieva/test_cases/screenshots/add_player/form-filled-in.png")
        Image.open("C:/Users/tpomo/Documents/GitHub/challenge_1_pomohaieva/test_cases/screenshots/add_player/form-filled-in.png").show()
        add_player.click_on_the_clear_button()
        add_player.assert_element_text(self.driver, add_player.name_field_xpath, "")
        add_player.assert_element_text(self.driver, add_player.surname_field_xpath, "")
        add_player.assert_element_text(self.driver, add_player.phone_field_xpath, "")
        add_player.assert_element_text(self.driver, add_player.age_field_xpath, "")
        add_player.assert_element_text(self.driver, add_player.name_field_xpath, "")
        add_player.assert_element_text(self.driver, add_player.main_position_field_xpath, "")
        self.driver.save_screenshot("C:/Users/tpomo/Documents/GitHub/challenge_1_pomohaieva/test_cases/screenshots/add_player/form-cleared.png")
        Image.open("C:/Users/tpomo/Documents/GitHub/challenge_1_pomohaieva/test_cases/screenshots/add_player/form-cleared.png").show()

    @classmethod
    def tearDown(self):
        self.driver.quit()
