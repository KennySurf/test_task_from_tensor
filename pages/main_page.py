from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):

    def go_to_contacts(self):
        self.open()
        self.click_element(MainPageLocators.CONTACT_LINK)

    def go_to_downloads_page(self):
        self.open()
        self.scroll(MainPageLocators.DOWNLOADS_LINK)
        self.click_element(MainPageLocators.DOWNLOADS_LINK)
