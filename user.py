class User:
    def __init__(self, name):
        self.name = name
        self.movies = []

    def __repr__(self):
        return f'User {self.name}'

    def watched_movies(self):
        movies_watched = list(filter(lambda x: x.watched, self.movies))
        return movies_watched
