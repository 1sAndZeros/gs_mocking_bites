from lib.MusicLibrary import *
from lib.Track import *

def test_add_tracks():
    my_library = MusicLibrary()
    track1 = Track('Title One', 'Artist One')
    my_library.add(track1)
    assert my_library.tracks == [track1]
    track2 = Track('Title Two', 'Artist Two')
    my_library.add(track2)
    assert my_library.tracks == [track1, track2]

def test_search():
    my_library = MusicLibrary()
    track1 = Track('Title One', 'Artist One')
    my_library.add(track1)
    track2 = Track('Title Two', 'Artist Two')
    my_library.add(track2)
    assert my_library.search('Title Two') == [track2]
    assert my_library.search('Title One') == [track1]
    assert my_library.search('Artist Two') == [track2]
    assert my_library.search('Artist One') == [track1]
    assert my_library.search('Artist') == [track1, track2]
    assert my_library.search('Title') == [track1, track2]
    assert my_library.search('Empty') == []