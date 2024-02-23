from .base_page import BasePage
from .locators import DownloadsPageLocators
import time
import os


class DownloadsPage(BasePage):
    def download_plugin(self):
        time.sleep(1)
        self.java_click_element(DownloadsPageLocators.PLUGINS_LINK)
        self.click_element(DownloadsPageLocators.DOWNLOADS_LINK)

    def check_downloaded_plugin_on_pc(self, timeout=30):
        download_path = os.path.join(os.getcwd(), 'downloads_folder')
        file_extension = ".crdownload"
        file_name = 'sbisplugin-setup-web.exe'
        download_complete = False
        end_time = time.time() + timeout

        while not download_complete and time.time() < end_time:
            files = [f for f in os.listdir(download_path) if f.endswith(file_extension) or f == file_name]
            download_complete = bool(files)
            time.sleep(1)

        if files:
            file_size = os.path.getsize(os.path.join(download_path, files[-1]))
            return file_size
        else:
            return 0
