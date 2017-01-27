import webbrowser


class Movie():
    """Movie Trailer Website

    Attributes:
        movie_title (str): Title of the movie.
        poster_image_url (str): Poster URL from IMDB.
        trailer_youtube_url (str): Movie trailer from Youtube.
    """

    def __init__(self, movie_title, poster_image_url, trailer_youtube_url):
        self.title = movie_title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
