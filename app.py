from movie import Movie
from user import User

user = User("Gage")

my_movie = Movie("The Matrix", "Sci-Fi", True)

user.movies.append(my_movie)

print(user)
print(user.watched_movies())
