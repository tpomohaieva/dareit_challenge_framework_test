from pages.base_page import BasePage


class LoginPage(BasePage):
    login_form_xpath = "//*[@id='__next']/form"
    login_form_title_xpath = "//*[@id='__next']//h5"
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[@type='submit']"
    remind_password_hyperlink_xpath = "//child::form//a"
    select_language_button_xpath = "//form//*[@role='button']"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
