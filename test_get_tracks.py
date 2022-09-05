from pages.main_page import MainPage


PLAYLIST_LINK = 'https://music.yandex.ru/users/simonivan24/playlists/1007'


class TestGetTracks():
    def test_guest_can_go_to_login_page(self, browser):
        link = PLAYLIST_LINK
        page = MainPage(browser, link)
        page.open()
        page.tracks_to_file()
