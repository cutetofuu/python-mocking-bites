import pytest
from lib.track import Track

"""
Given empty strings as title and artist
Raises an error
"""
def test_raises_error_given_empty_strings():
    with pytest.raises(Exception) as err:
        Track("", "")
    error_message = str(err.value)
    assert error_message == "You have not entered a track."

"""
Given a title and an artist
#title returns the title
"""
def test_returns_title_given_title_and_artist():
    track = Track("Title 1", "Artist 1")
    assert track.title == "Title 1"

"""
Given a title and an artist
#artist returns the artist
"""
def test_returns_title_given_title_and_artist():
    track = Track("Title 1", "Artist 1")
    assert track.artist == "Artist 1"

"""
Given a title, an artist 
and a partial keyword that matches the title
#matches returns True
"""
def test_returns_true_given_title_artist_and_matching_partial_keyword():
    track = Track("This is a song title", "Artist 1")
    assert track.matches("on") == True

"""
Given a title, an artist 
and a keyword that matches the title
#matches returns True
"""
def test_returns_true_given_title_artist_and_matching_keyword():
    track = Track("This is a song title", "Artist 1")
    assert track.matches("song") == True

"""
Given a title, an artist 
and a keyword that has no matches
#matches returns False
"""
def test_returns_false_given_title_artist_and_keyword_with_no_matches():
    track = Track("This is a song title", "Artist 1")
    assert track.matches("happy") == False