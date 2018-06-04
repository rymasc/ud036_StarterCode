class Movie(object):
    def __init__(self, title, img_link, trailer_link):
        self.title = title
        self.poster = img_link
        self.trailer = trailer_link

    def showTrailer():
        webbrowser.open(self.trailer)
