from selenium import webdriver

import constants
from base_page import BasePage


class DashboardPage(BasePage):

    def click_on_orderguide(self):
        return super().click_element_by_link_text("Order Guide")

    def click_on_orderguidedashboard(self):
        return super().click_element_by_link_text("Order Guide Dashboard")

    def click_on_wrenchicon(self):
        return super().click_button_with_id(constants.WRENCHICON_ID)

    def click_on_signinasstore(self):
        return super().click_element_by_link_text(constants.SIGNINASSTORE)


