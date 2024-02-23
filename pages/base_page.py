from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def get_element_text(self, locator):
        element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(locator))
        return element.text

    def get_elements_text(self, locator):
        elements = WebDriverWait(self.browser, 10).until(
            EC.presence_of_all_elements_located(locator))
        return [element.text for element in elements]


    def click_element(self, locator):
        element = WebDriverWait(self.browser, 10 ).until(
            EC.element_to_be_clickable(locator))
        element.click()

    def java_click_element(self, locator):
        element = WebDriverWait(self.browser, 10 ).until(
            EC.element_to_be_clickable(locator))
        self.browser.execute_script('arguments[0].click();', element)

    def switch_to_tab(self, tab_number):
        handles = self.browser.window_handles
        if len(handles) > tab_number:
            self.browser.switch_to.window(handles[tab_number])
        else:
            raise ValueError(f'Tab with number {tab_number} does not exist')

    def scroll(self, locator):
        element = self.browser.find_element(*locator)
        self.browser.execute_script(
            'return arguments[0].scrollIntoView(true);', element
        )

    def compare_title(self, title):

        expected_title_part = title
        current_title = self.browser.title

        assert expected_title_part in current_title

    def compare_url(self, expected_url_part):

        WebDriverWait(self.browser, 10).until(
            EC.url_contains(expected_url_part)
        )

        current_url = self.browser.current_url

        assert expected_url_part in current_url, 'no'

    def is_element_present(self, locator):
        try:
            self.browser.find_element(*locator)
        except NoSuchElementException:
            return False
        return True
