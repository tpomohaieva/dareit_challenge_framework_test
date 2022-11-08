from pages.base_page import BasePage


class AddPlayerPage(BasePage):
    page_title_xpath = "//header//h6"
    main_page_link_xpath = "//ul[1]//div[@role='button'][1]"
    players_link_xpath = "//ul[1]//div[@role='button'][2]"
    language_select_xpath = "//ul[2]//div[@role='button'][1]"
    sign_out_link_xpath = "//ul[2]//div[@role='button'][2]"
    add_player_form_xpath = "//*[@id='__next']//form"
    add_player_form_title_xpath = "//form//*[contains(@class, 'h5')]"
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





