from lib.music_library import MusicLibrary
from lib.track import Track

"""
Given 1 track
#self.tracks returns a list with 1 track
"""
def test_returns_list_with_1_track_given_1_track():
    music_library = MusicLibrary()
    track = Track("Wannabe", "Spice Girls")
    music_library.add(track)
    assert music_library.tracks == [track]

"""
Given 3 tracks
#self.tracks returns a list with 3 tracks
"""
def test_returns_list_with_3_tracks_given_3_tracks():
    music_library = MusicLibrary()
    track_1 = Track("Wannabe", "Spice Girls")
    track_2 = Track("Bye Bye Bye", "NSYNC")
    track_3 = Track("Everybody", "Backstreet Boys")
    music_library.add(track_1)
    music_library.add(track_2)
    music_library.add(track_3)
    assert music_library.tracks == [track_1, track_2, track_3]

"""
Given 3 tracks and a keyword with no matches
#search returns an empty list
"""
def test_returns_list_with_1_tracks_given_3_tracks_and_keyword_with_no_matches():
    music_library = MusicLibrary()
    track_1 = Track("Wannabe", "Spice Girls")
    track_2 = Track("Bye Bye Bye", "NSYNC")
    track_3 = Track("Barbie Girl", "Aqua")
    music_library.add(track_1)
    music_library.add(track_2)
    music_library.add(track_3)
    assert music_library.search("wooooo") == []

"""
Given 3 tracks and a keyword with 1 match
#search returns a list with 1 track
"""
def test_returns_list_with_1_tracks_given_3_tracks_and_keyword_with_1_match():
    music_library = MusicLibrary()
    track_1 = Track("5, 6, 7, 8", "Steps")
    track_2 = Track("Bye Bye Bye", "NSYNC")
    track_3 = Track("Everybody", "Backstreet Boys")
    music_library.add(track_1)
    music_library.add(track_2)
    music_library.add(track_3)
    assert music_library.search("Bye") == [track_2]

"""
Given 3 tracks and a keyword with 2 matches
#search returns a list with 2 tracks
"""
def test_returns_list_with_1_tracks_given_3_tracks_and_keyword_with_2_matches():
    music_library = MusicLibrary()
    track_1 = Track("Wannabe", "Spice Boys")
    track_2 = Track("Bye Bye Bye", "NSYNC")
    track_3 = Track("Everybody", "Backstreet Boys")
    music_library.add(track_1)
    music_library.add(track_2)
    music_library.add(track_3)
    assert music_library.search("Boys") == [track_1, track_3]