import webbrowser

class Movie ():
    """I am just testing if this works"""
    VALID_RATINGS = ["(G)","(PG)","(PG13)","(M18)","(R21)"]
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, movie_overview, movie_rating):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.overview = movie_overview
        self.rating = movie_rating

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
