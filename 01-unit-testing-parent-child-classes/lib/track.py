import re

class Track:
    def __init__(self, title, artist):
        if title == "" or artist == "":
            raise Exception("You have not entered a track.")
        else:
            self.title = title
            self.artist = artist

    def matches(self, keyword):
        title_matches = re.findall(keyword, self.title)
        artist_matches = re.findall(keyword, self.artist)

        return True if title_matches != [] or artist_matches != [] else False