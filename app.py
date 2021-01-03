import json
import os

from user import User


def menu():
    name = input("Enter Name: ").capitalize()
    filename = f'{name}.txt'
    if file_exists(filename):
        with open(filename, 'r') as f:
            json_data = json.load(f)
        user = User.from_json(json_data)
    else:
        user = User(name)

    user_input = input("Enter 'a' to add a movie, 'i' to see the list of movies,\n "
                       "'w' to set movie as watched, 'd' to delete a movie, 'l' to see the list of watched movies,\n"
                       "'s' to save or 'q' to quit: ")
    while user_input != 'q':
        if user_input == 'a':
            movie_name = input("Enter the movie name: ")
            movie_genre = input("Enter the movie genre: ")
            user.add_movie(movie_name, movie_genre)
        elif user_input == 'i':
            for movie in user.movies:
                print(f"Name: {movie.name} Genre: {movie.genre} Watched {movie.watched}")
        elif user_input == 'w':
            movie_name = input("Enter the movie name to set as watched: ")
            user.set_watched(movie_name)
        elif user_input == 'd':
            movie_name = input("Enter the movie name to delete: ")
            user.delete_movie(movie_name)
        elif user_input == 'l':
            for movie in user.watched_movies():
                print(f"Name: {movie.name} Genre: {movie.genre} Watched {movie.watched}")
        elif user_input == 's':
            with open(filename, 'w') as f:
                json.dump(user.json(), f)

        user_input = input("Enter 'a' to add a movie, 's' to see the list of movies,\n "
                           "'w' to set movie as watched, 'd' to delete a movie,\n"
                           "'l' to see the list of watched movies,\n"
                           "or 'q' to save and quit: ")


def file_exists(filename):
    return os.path.isfile(filename)


menu()
