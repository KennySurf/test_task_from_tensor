from .base_page import BasePage
from .locators import TensorPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TensorPage(BasePage):
    def scroll_to_power_block(self):
        self.switch_to_tab(1)
        self.scroll(TensorPageLocators.POWER_BLOCK)
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(TensorPageLocators.POWER_BLOCK)
        )

    def is_power_block_present(self):
        return self.is_element_present(TensorPageLocators.POWER_BLOCK)

    def go_to_about_page(self):
        about_link = self.browser.find_element(*TensorPageLocators.ABOUT_LINK)
        about_link.click()
