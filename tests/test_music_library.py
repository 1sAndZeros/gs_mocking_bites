from lib.MusicLibrary import *
from unittest.mock import Mock

def test_add_track():
    my_library = MusicLibrary()
    track1 = Mock()
    track1.title = 'Title One'
    track1.artist = 'Artist One'
    my_library.add(track1)
    assert my_library.tracks == [track1]
    track2 = Mock()
    track2.title = 'Title Two'
    track2.artist = 'Artist Two'
    my_library.add(track2)
    assert my_library.tracks == [track1, track2]

def test_search():
    my_library = MusicLibrary()
    track1 = Mock()
    track1.matches.return_value = False
    my_library.add(track1)
    track2 = Mock()
    track2.matches.return_value = True
    my_library.add(track2)
    assert my_library.search('Two') == [track2]