from pages.base_page import BasePage


class RemindPasswordPage(BasePage):
    remind_pw_form_title_xpath = "//h5"
    remind_pw_form_title_text = "Remind password"
    email_field_xpath = "//*[@name='email']"
    send_button_xpath = "//*[@type='submit']"
    remind_pw_page_url = "https://scouts.futbolkolektyw.pl/login"
    expected_title = 'Remind password'

    def title_of_the_page(self):
        self.wait_for_element_to_be_clickable(self.send_button_xpath)
        assert self.driver.title == self.expected_title
