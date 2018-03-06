class Movie:
    """
    The model for holding information about a movie.
    """
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        """
        :param title: Movie title
        :param poster_image_url: URL to the movie poster
        :param trailer_youtube_url: URL to the trailer from youtube.
        """
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
