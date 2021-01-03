from user import User

user = User.load_from_file("Gage.txt")

print(user.movies)

