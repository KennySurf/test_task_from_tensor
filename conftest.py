import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import os

download_directory = os.path.join(os.path.dirname(__file__), 'downloads_folder')
prefs = {'download.default_directory': download_directory}


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome',
                     help='Choose browser')
    parser.addoption('--language', action='store', default='en',
                     help='Choose language')


@pytest.fixture(scope='session')
def browser(request):
    browser_name = request.config.getoption('browser')
    user_language = request.config.getoption('language')
    browser = None

    if browser_name == 'chrome':
        options = ChromeOptions()

        options.add_experimental_option('prefs', prefs)
        options.add_argument(f'--lang={user_language}')

        print('\nstarting chrome browser..')
        browser = webdriver.Chrome(options=options)

    elif browser_name == 'firefox':
        options = FirefoxOptions()
        profile = webdriver.FirefoxProfile()
        profile.set_preference('intl.accept_languages', user_language)
        options.profile = profile

        options.add_experimental_option('prefs', prefs)

        print('\nstarting firefox browser..')
        browser = webdriver.Firefox(options=options)

    else:
        raise pytest.UsageError('--browser_name should be chrome of firefox')

    yield browser
    print('\nbrowser quit..')
    browser.quit()
