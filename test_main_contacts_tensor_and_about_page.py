import pytest
from .pages.main_page import MainPage
from .pages.contacts_page import ContactsPage
from .pages.tensor_page import TensorPage
from .pages.about_page import AboutPage


class TestMainPage:

    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.main_page = MainPage(browser, "https://sbis.ru/")

    def test_go_to_contacts(self):
        self.main_page.go_to_contacts()


class TestContactPage:

    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.contacts_page = ContactsPage(browser, 'https://sbis.ru/contacts')

    def test_click_tensor_banner(self):
        self.contacts_page.click_tensor_banner()


class TestTensorPage:

    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.tensor_page = TensorPage(browser, 'https://tensor.ru/')

    def test_check_power_block(self):
        self.tensor_page.scroll_to_power_block()
        assert self.tensor_page.is_power_block_present, \
            'power block is not present on the page'

    def test_go_to_about(self):
        self.tensor_page.go_to_about_page()


class TestAboutPage:

    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.about_page = AboutPage(browser, "https://tensor.ru/about" )

    def test_check_photos(self):
        self.about_page.scroll_to_photos_block()
        assert self.about_page.is_photos_block_present, \
            'photos block is not present on the page'

    def test_check_photos_height_and_width(self):
        self.about_page.check_photos_height_width()
