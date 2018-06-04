import webbrowser


class Movie(object):
    """docstring for ."""
    def __init__(self, title, img_link, trailer_link):
        self.title = title
        self.poster_image_url = img_link
        self.trailer_youtube_url = trailer_link

    def showTrailer():
        webbrowser.open(self.trailer)
