from selenium.webdriver.common.by import By


from time import sleep


from .locators import MainPageLocators


class MainPage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)
        self.browser.find_element(*MainPageLocators.CROSS).click()

    def get_num_of_tracks(self):
        self.browser.execute_script(
            'window.scrollTo(0, document.body.scrollHeight);')
        sleep(1)
        num_of_tracks = self.browser.find_elements(
            By.CLASS_NAME, 'd-track')[-1].get_attribute("data-id")
        self.browser.execute_script('window.scrollTo(0, 0);')
        return int(num_of_tracks) + 1

    def tracks_to_file(self):
        tracks_file = open("tracks_file.txt", "w+", encoding='utf-8')
        for i in range(1, self.get_num_of_tracks()):
            track = self.browser.find_element(
                By.CSS_SELECTOR, f'[data-id="{i}"]')
            artists = track.find_elements(*MainPageLocators.ARTISTS)

            artists_names = ''
            for artist in artists:
                artists_names += artist.get_attribute("title")
                if artist.text != artists[-1].text:
                    artists_names += '; '  # separator between artists

            track_name = track.find_element(*MainPageLocators.TRACK_NAME)

            # line in file
            tracks_file.write(f'{artists_names} - {track_name.text}\n')

            self.browser.execute_script("arguments[0].scrollIntoView();",
                                        track)
        tracks_file.close()
