# Jukebox
# Very simple, no display
# Three buttons: prev, next, play/pause
# Attached cash module
# Every song costs the same amount
# No way to return change
# Example: If every song cost $2, I put in $5, I get 2 songs. If I put in another $5, I get 3 more songs.



# jukebox.py

from main.cash_io import CashIO
from unittest import TestCase


class Jukebox(object):
    """
    This class represents the state of an iPod Shuffle-like Jukebox. To use this Jukebox, a customer inserts money
    into the jukebox.

    The hardware behaves based on the state of this class, i.e. if is_playing is set to true, the current song will
    start playing.
    """
    _songs_left = 0
    _value_left = 0
    _current_song = 0
    _currency_accepted = 20

    # 1. Use default params for params not required during init

    def __init__(self, songs_list, cost_of_song, cash_io=CashIO()):
        self._songs_list = songs_list
        self._cost_of_song = cost_of_song
        self.cash_io = cash_io
        self._current_song = 0
        self._is_playing = False

    def add_money(self):
        value = self.cash_io.scan_bill()

        if value > _currency_accepted:
            self.cash_io.reject_bill()
        else:
            self._value_left = value / self._cost_of_song

    def get_song(self):
        return self._songs_list[self._current_song]

    def is_playing(self):
        if self._is_playing is True:
            return 'yes'
        elif self._is_playing is False:
            return 'no'

        return None

    def toggle_play_pause(self):
        if self._is_playing:
            self._is_playing = False
        else:
            self._is_playing = True

    def select_next_song(self):
        if self._value_left >= self._cost_of_song:
            self._value_left -= self._cost_of_song
            self._songs_left -= 1
            self._current_song += 1

    def select_prev_song(self):
        if self._value_left >= self._cost_of_song:
            self._value_left -= self._cost_of_song
            self._songs_left -= 1
            self._current_song -= 1

    def print_all_songs(self):
        for song in song_list:
            print(song)

    def event_song_finished(self):
        self._is_playing = False
        self.select_next_song()
        self.toggle_play_pause()



        # Coding STD: PEP


# test_jukebox.py

# 1. Not adequate tests
# 2.
#

class TestJukebox(TestCase):
    def test_it_can_init(self):
        songs = [
            'Song 1',
            'Song 2',
            'Song 3',
        ]
        jukebox = Jukebox(songs, 2)
        self.assertTrue(jukebox.setup())

    def test_it_prints_all_songs(self):
        songs = [
            'Song 1',
            'Song 2',
            'Song 3',
        ]
        jukebox = Jukebox(songs, 2)
        jukebox.print_all_songs()

    def test_add_money(self):
        songs = [
            'Song 1',
            'Song 2',
            'Song 3',
        ]
        cash_io = CashIO()
        cash_io.scan_bill = lambda: 20

        jukebox = Jukebox(songs, 2, cash_io)
        # self.cash_io.scan_bill=20
        self.assertTrue(jukebox.add_money())


# cash_io.py
# VENDOR CODE
"""
usb_in = sys.stdin
usb_out = sys.stdout

real = cachIO()
mock = Mock()
real = mock.scan_bill()

mock = Mock(CashIO)
mock.scan_bill.return_value = 20
"""


class CashIO(object):
    def scan_bill(self):
        usb_out.write('SCAN_BILL')
        response = usb_in.readline().lower()
        if response == 'stuck_bill':
            raise StuckBillException()
        else:
            return int(response)

    def reject_bill(self):
        usb_out.write('REJECT_BILL')
        response = usb_in.readline().lower()
        if response == 'ok':
            return True
        elif response == 'stuck_bill':
            raise StuckBillException()
        else:
            return False


class StuckBillException(Exception):
    pass
