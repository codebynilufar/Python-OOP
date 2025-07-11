class Movie:
    def __init__(self, title, genre, duration, rating) -> None:
        self.title = title
        self.genre = genre
        self.duration = duration
        self.rating = rating

movie = Movie("Harry Potter and the Sorcerer's Stone", "2h 32m", "Fantacy", 7.6 )

print(f"Title: {movie.title}")
print(f"Genre: {movie.genre}")
print(f"Duration: {movie.duration}")
print(f"Rating: {movie.rating}")
