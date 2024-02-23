import pytest
from .pages.main_page import MainPage
from .pages.downloads_page import DownloadsPage


class TestMainPage:

    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.main_page = MainPage(browser, "https://sbis.ru/")

    def test_user_click_downloads_link(self):
        self.main_page.go_to_downloads_page()


class TestDownloadsPage:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.downloads_page = DownloadsPage(browser, "https://sbis.ru/download?tab=ereport&innerTab=ereport25")

    def test_user_must_be_download_plugin(self):
        self.downloads_page.download_plugin()
        actual_size = self.downloads_page.check_downloaded_plugin_on_pc()
        assert actual_size == 8553592, \
            'file is missing or file size does not match'
