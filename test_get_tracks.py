from .pages.main_page import MainPage


PLAYLIST_LINK = 'https://music.yandex.ru/users/sasha28200461/playlists/3'


class TestGetTracks():
    def test_guest_can_go_to_login_page(self, browser):
        link = PLAYLIST_LINK
        page = MainPage(browser, link)
        page.open()
        page.tracks_to_file()
