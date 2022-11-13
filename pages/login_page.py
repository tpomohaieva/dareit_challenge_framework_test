from pages.base_page import BasePage


class LoginPage(BasePage):
    login_form_xpath = "//*[@id='__next']/form"
    login_form_title_xpath = "//*[@id='__next']//h5"
    login_form_title_text = "Scouts Panel"
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[@type='submit']"
    remind_password_hyperlink_xpath = "//child::form//a"
    select_language_button_xpath = "//form//*[@role='button']"
    login_page_url = "https://scouts-test.futbolkolektyw.pl/login"
    expected_title = 'Scouts panel - sign in'

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_the_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_the_page(self):
        assert self.get_page_title(self.login_page_url) == self.expected_title



