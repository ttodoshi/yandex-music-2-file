from selenium.webdriver.common.by import By


class MainPageLocators:
    CROSS = (By.CLASS_NAME, 'd-icon_cross-big')
    TRACK_NAME = (By.CLASS_NAME, 'd-track__title')
    ARTISTS = (By.CSS_SELECTOR, '.d-track__artists .deco-link')
