import time

from pages.base_page import BasePage


class Dashboard(BasePage):
    page_title_xpath = "//header//h6"
    main_page_link_xpath = "//ul[1]//div[@role='button'][1]"
    players_link_xpath = "//ul[1]//div[@role='button'][2]"
    language_select_xpath = "//ul[2]//div[@role='button'][1]"
    sign_out_link_xpath = "//ul[2]//div[@role='button'][2]"
    players_count_panel_xpath = "//main/div[2]/div[1]/div"
    players_count_label_xpath = "//main/div[2]/div[1]/div/div[1]"
    players_count_value_xpath = "//main/div[2]/div[1]//b"
    matches_count_panel_xpath = "//main/div[2]/div[2]/div"
    matches_count_label_xpath = "//main/div[2]/div[2]/div/div[1]"
    matches_count_value_xpath = "//main/div[2]/div[2]//b"
    reports_count_panel_xpath = "//main/div[2]/div[3]/div"
    reports_count_label_xpath = "//main/div[2]/div[3]/div/div[1]"
    reports_count_value_xpath = "//main/div[2]/div[3]//b"
    events_count_panel_xpath = "//main/div[2]/div[4]/div"
    events_count_label_xpath = "//main/div[2]/div[4]/div/div[1]"
    events_count_value_xpath = "//main/div[2]/div[4]//b"
    scouts_panel_xpath = "//main/div[3]/div[1]/div"
    scouts_logo_xpath = "//div[@title='Logo Scouts Panel']"
    scouts_title_xpath = "//main/div[3]/div[1]//h2"
    scouts_desc_xpath = "//h2//following-sibling::p"
    scouts_dev_team_link_xpath = "//main/div[3]/div[1]//a"
    shortcuts_panel_xpath = "//main/div[3]/div[2]/div"
    shortcuts_title_xpath = "//main/div[3]/div[2]//h2"
    shortcuts_add_player_link_xpath = "//a[contains(@href,'add')]"
    activity_panel_xpath = "//main/div[3]/div[3]/div"
    activity_title_xpath = "//main/div[3]/div[3]//h2"
    activity_last_created_player_link_xpath = "//h6[1]//following-sibling::a[1]"
    activity_last_updated_player_link_xpath = "//h6[2]//following-sibling::a[1]"
    activity_last_created_match_link_xpath = "//h6[3]//following-sibling::a[1]"
    activity_last_updated_match_link_xpath = "//h6[4]//following-sibling::a[1]"
    activity_last_updated_report_link_xpath = "//h6[5]//following-sibling::a[1]"
    dashboard_page_url = "https://scouts-test.futbolkolektyw.pl/"
    expected_title = "Scouts panel"

    def title_of_the_page(self):
        time.sleep(5)
        assert self.get_page_title(self.dashboard_page_url) == self.expected_title

    def click_on_add_player(self):
        self.click_on_the_element(self.shortcuts_add_player_link_xpath)
