class User:
    def __init__(self, username, email, is_active):
        self.username = username
        self.email = email
        self.is_active = is_active

    def activate(self):
        self.is_active = True
        print(f"{self.username} faollashtirildi ✅")

    def deactivate(self):
        self.is_active = False
        print(f"{self.username} bloklandi ❌")

user1 = User("nilufar23", "nilufar@mail.com", False)
user1.activate()
user1.deactivate()


