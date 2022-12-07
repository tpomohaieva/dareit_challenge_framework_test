from pages.base_page import BasePage


class AddPlayerPage(BasePage):
    page_title_xpath = "//header//h6"
    main_page_link_xpath = "//ul[1]//div[@role='button'][1]"
    players_link_xpath = "//ul[1]//div[@role='button'][2]"
    language_select_xpath = "//ul[2]//div[@role='button'][1]"
    sign_out_link_xpath = "//ul[2]//div[@role='button'][2]"
    add_player_form_xpath = "//*[@id='__next']//form"
    add_player_form_title_xpath = "//form//*[contains(@class, 'h5')]"
    player_added_form_title_text = "Edit player Test Testowski"
    email_field_xpath = "//input[@name='email']"
    name_field_xpath = "//input[@name='name']"
    surname_field_xpath = "//input[@name='surname']"
    phone_field_xpath = "//input[@name='phone']"
    weight_field_xpath = "//input[@name='weight']"
    height_field_xpath = "//input[@name='height']"
    age_field_xpath = "//input[@name='age']"
    leg_field_xpath = "//input[@name='leg']"
    club_field_xpath = "//input[@name='club']"
    level_field_xpath = "//input[@name='level']"
    main_position_field_xpath = "//input[@name='mainPosition']"
    second_position_field_xpath = "//input[@name='secondPosition']"
    district_field_xpath = "//*[contains(@id,'select-district')]"
    achievements_field_xpath = "//input[@name='achievements']"
    add_lang_button_xpath = "//button[@aria-label='Add language']"
    laczy_nas_pilka_field_xpath = "//input[@name='webLaczy']"
    _90_minut_field_xpath = "//input[@name='web90']"
    facebook_field_xpath = "//input[@name='webFB']"
    add_youtube_button_xpath = "//button[@aria-label='Add link to Youtube']"
    submit_button_xpath = "//button[@type='submit']"
    clear_button_xpath = "//button[@type='submit']//following-sibling::button"
    add_player_url = "https://scouts.futbolkolektyw.pl/en/players/add"
    expected_title = "Add player"
    expected_title_player_added = "Edit player Test Testowski"
    progress_bar_toaster_xpath = "//*[@role='alert']"
    required_message_xpath = "//p[contains(@class, 'required')]"

    def title_of_the_page(self):
        assert self.get_page_title(self.add_player_url) == self.expected_title

    def type_in_email(self, email):
        self.field_send_keys(self.email_field_xpath, email)

    def type_in_name(self, name):
        self.field_send_keys(self.name_field_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.surname_field_xpath, surname)

    def type_in_phone(self, phone):
        self.field_send_keys(self.phone_field_xpath, phone)

    def type_in_age(self, age):
        self.field_send_keys(self.age_field_xpath, age)

    def type_in_club(self, club):
        self.field_send_keys(self.club_field_xpath, club)

    def type_in_main_position(self, main_position):
        self.field_send_keys(self.main_position_field_xpath, main_position)

    def click_on_the_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)

    def click_on_the_clear_button(self):
        self.click_on_the_element(self.clear_button_xpath)

    def click_on_the_name_field(self):
        self.click_on_the_element(self.name_field_xpath)

    def player_added_title_of_the_page(self):
        self.wait_for_element_to_be_visible(self.progress_bar_toaster_xpath)
        assert self.driver.title == self.expected_title_player_added

    def show_name_required_error(self):
        self.wait_for_element_to_be_visible(self.required_message_xpath)
        self.assert_element_text(self.driver, self.required_message_xpath, "Required")

