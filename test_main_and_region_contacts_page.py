import pytest
from .pages.main_page import MainPage
from .pages.contacts_page import ContactsPage


class TestMainPage:

    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.main_page = MainPage(browser, "https://sbis.ru/")

    def test_go_to_contacts(self):
        self.main_page.go_to_contacts()

class TestContactsPage:

    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.contacts_page = ContactsPage(browser, 'https://sbis.ru/contacts')

    def test_is_region_guest_true(self):
        assert self.contacts_page.is_region_correct('Тюменская обл.'), \
            'region is not correct'

    def test_check_partner_block(self):
        assert self.contacts_page.is_partner_block_present(), \
            'partner link is not present on the page'

    def test_region_and_partners_must_be_changed(self):
        assert self.contacts_page.change_region_and_partners(), \
            'the region has not changed'

    def test_url_and_title_must_be_changed(self):
        self.contacts_page.compare_url_after_changing_region()
        self.contacts_page.compare_title_after_changing_region()
