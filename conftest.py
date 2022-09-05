import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store',
                     default='ru', help='Choose language')


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption('language')

    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_experimental_option(
        'prefs', {'intl.accept_languages': user_language})
    print("\nstart chrome browser for test..")
    browser = webdriver.Chrome(options=chrome_options)

    browser.implicitly_wait(5)
    yield browser
    browser.quit()
