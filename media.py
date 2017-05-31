# coding: utf-8


class Movie(object):
    """
    Movie is a class to describe a film.
    The constructor requires 3 parameters.
    
    Attributes:
        title: the title of the movie
        poster_image_url: the url of the movie's poster image
        trailer_youtube_url: the youtube url of the movie's trailer
    """

    def __init__(self, title, image, trailer):
        self.title = title
        # self.storyline
        self.poster_image_url = image
        self.trailer_youtube_url = trailer
