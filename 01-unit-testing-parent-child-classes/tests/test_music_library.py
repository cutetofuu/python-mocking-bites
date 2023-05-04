from lib.music_library import MusicLibrary
from unittest.mock import Mock

"""
#self.tracks initially returns an empty list
when no tracks have been added yet
"""
def test_initially_returns_empty_list_given_no_tracks():
    music_library = MusicLibrary()
    assert music_library.tracks == []

"""
Given 1 mock track
Returns a list with 1 track
"""
def test_returns_list_with_1_track_given_1_mock_track():
    music_library = MusicLibrary()
    
    # track_1 = FakeTrack("Title 1", "Artist 1")
    track_1 = Mock()

    music_library.add(track_1)
    assert music_library.tracks == [track_1]

"""
Given multiple mock tracks
Returns a list of multiple tracks
"""
def test_returns_multiple_tracks_given_multiple_mock_tracks():
    music_library = MusicLibrary()

    # track_1 = FakeTrack("Track 1", "Artist 1")
    # track_2 = FakeTrack("Track 2", "Artist 2")
    # track_3 = FakeTrack("Track 3", "Artist 3")
    track_1 = Mock()
    track_2 = Mock()
    track_3 = Mock()

    music_library.add(track_1)
    music_library.add(track_2)
    music_library.add(track_3)
    assert music_library.tracks == [track_1, track_2, track_3]

"""
Given multiple mock tracks 
and a keyword with no matches
#search returns an empty list
"""
def test_returns_empty_list_given_multiple_mock_tracks_and_keyword():
    music_library = MusicLibrary()

    track_1 = Mock()
    track_1.matches.return_value = False

    track_2 = Mock()
    track_2.matches.return_value = False

    track_3 = Mock()
    track_3.matches.return_value = False

    music_library.add(track_1)
    music_library.add(track_2)
    music_library.add(track_3)
    assert music_library.search("ack") == []

"""
Given multiple mock tracks 
and a keyword with 1 match
#search returns a list with one track
"""
def test_returns_list_with_one_track_given_multiple_mock_tracks_and_keyword():
    music_library = MusicLibrary()

    track_1 = Mock()
    track_1.matches.return_value = False

    track_2 = Mock()
    track_2.matches.return_value = True

    track_3 = Mock()
    track_3.matches.return_value = False

    music_library.add(track_1)
    music_library.add(track_2)
    music_library.add(track_3)
    assert music_library.search("ack") == [track_2]

"""
Given multiple mock tracks 
and a keyword with multiple matches
#search returns a list with multiple tracks
"""
def test_returns_list_with_multiple_tracks_given_multiple_mock_tracks_and_keyword():
    music_library = MusicLibrary()

    track_1 = Mock()
    track_1.matches.return_value = True

    track_2 = Mock()
    track_2.matches.return_value = False

    track_3 = Mock()
    track_3.matches.return_value = True

    music_library.add(track_1)
    music_library.add(track_2)
    music_library.add(track_3)
    assert music_library.search("ack") == [track_1, track_3]

# class FakeTrack:
#     def __init__(self, title, artist):
#         self.title = title
#         self.artist = artist