from .base_page import BasePage
from .locators import ContactPageLocators
from time import sleep


class ContactsPage(BasePage):
    def click_tensor_banner(self):
        self.click_element(ContactPageLocators.BANNER_LINK)

    def is_region_correct(self, expected_region):
        actual_region = self.get_element_text(ContactPageLocators.REGION_LINK)
        return expected_region in actual_region

    def is_partner_block_present(self):
        return self.is_element_present(ContactPageLocators.PARTNER_BLOCK_LINK)

    def change_region_and_partners(self):
        first_partners_list = self.get_elements_text(ContactPageLocators.PARTNERS_LINK)[:]

        self.click_element(ContactPageLocators.REGION_LINK)
        self.java_click_element(ContactPageLocators.REQUIRED_REGION_LINK)

        sleep(1)
        second_partners_list = self.get_elements_text(ContactPageLocators.PARTNERS_LINK)
        return set(first_partners_list) != set(second_partners_list)

    def compare_url_after_changing_region(self):
        self.compare_url('kamchatskij-kraj')

    def compare_title_after_changing_region(self):
        self.compare_title('Камчатский край')
