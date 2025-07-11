class User:
    def __init__(self, username, email, is_active) -> None:
        self.username = username
        self.email = email
        self.is_active = is_active

user = User("examole01", "example@gmail.com", "False")
print(f"Username: {user.username}")
print(f"Email: {user.email}")
print(f"{user.is_active}")