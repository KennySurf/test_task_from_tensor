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
        download_path = os.path.join(os.path.dirname(__file__), '..' + '/downloads_folder')
        file_extension = ".crdownload"
        file_name = 'sbisplugin-setup-web.exe'
        download_complete = False
        end_time = time.time() + timeout

        while not download_complete and time.time() < end_time:
            time.sleep(1)
            files = [f for f in os.listdir(download_path) if f.endswith(file_extension) or f == file_name]
            download_complete = bool(files)

        self.size_on_download_page_in_bytes = int(float(self.get_element_text(DownloadsPageLocators.DOWNLOADS_LINK).split()[2]) * 1024 * 1024)
        self.tolerance_in_bytes = 10485.76


        if files:
            return os.path.getsize(os.path.join(download_path, files[0]))
        else:
            return 0
