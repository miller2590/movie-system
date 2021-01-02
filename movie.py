class Movie:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        self.director = "Wachowski"

    def __repr__(self):
        return f'Movie: {self.name}\n' \
               f'Genre: {self.genre}\n' \
               f'Director: {self.director}'
