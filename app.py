from user import User

user = User("Gage")

user.add_movie('Die Hard', 'Action')
user.add_movie('The Interview', 'Comedy')

user.save_to_file()
