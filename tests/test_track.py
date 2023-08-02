from lib.Track import *

def test_track_initialised():
    track1 = Track('Title One', 'Artist One')
    assert track1.title == 'Title One'
    assert track1.artist == 'Artist One'

def test_matches():
    track1 = Track('Title One', 'Artist One')
    track2 = Track('Title Two', 'Artist Two')
    assert track1.matches('Title') == True
    assert track1.matches('Artist') == True
    assert track1.matches('One') == True
    assert track1.matches('Two') == False
    assert track1.matches('Hello') == False
    assert track2.matches('Title') == True
    assert track2.matches('Artist') == True
    assert track2.matches('One') == False
    assert track2.matches('Two') == True
    assert track2.matches('Hello') == False