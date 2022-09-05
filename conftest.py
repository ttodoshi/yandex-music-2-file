import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import selenium.webdriver.edge.options as msedge_options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or msedge")
    parser.addoption('--language', action='store',
                     default='ru', help='Choose language')


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption('language')

    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_experimental_option(
            'prefs', {'intl.accept_languages': user_language})
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=chrome_options)
    elif browser_name == "msedge":
        edge_options = msedge_options.Options()
        edge_options.add_argument("--start-maximized")
        edge_options.add_experimental_option(
            'prefs', {'intl.accept_languages': user_language})
        print("\nstart msedge browser for test..")
        browser = webdriver.Edge(options=edge_options)

    else:
        raise pytest.UsageError("--browser_name should be chrome or msedge")

    browser.implicitly_wait(5)
    yield browser
    browser.quit()
