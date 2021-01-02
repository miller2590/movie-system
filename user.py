from movie import Movie


class User:
    def __init__(self, name):
        self.name = name
        self.movies = []

    def __repr__(self):
        return f'User {self.name}'

    def add_movie(self, name, genre):
        self.movies.append(Movie(name, genre, False))

    def delete_movie(self, name):
        self.movies = list(filter(lambda x: x.name != name, self.movies))

    def watched_movies(self):
        movies_watched = list(filter(lambda x: x.watched, self.movies))
        return movies_watched

    def save_to_file(self):
        with open(f'{self.name}.txt', 'w') as f:
            f.write(self.name + '\n')
            for movie in self.movies:
                f.write(f'{movie.name},{movie.genre},{str(movie.watched)}\n')
