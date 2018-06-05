import webbrowser


class Movie(object):
    """The Movie class instantiates movie objects using the movie title, poster
    image url, and youtube trailer url as strings
    args:
        title        (str): Movie title
        img_link     (str): Movie Poster Image URL
        trailer_link (str): Movie Trailer YouTube URL """
    def __init__(self, title, img_link, trailer_link):
        self.title = title
        self.poster_image_url = img_link
        self.trailer_youtube_url = trailer_link

    def showTrailer():
        webbrowser.open(self.trailer)
