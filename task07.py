class Movie:
    def __init__(self, title, genre, duration, rating) -> None:
        self.title = title
        self.genre = genre
        self.duration = duration
        self.rating = rating
    def show_summary(self) -> str:
        return f"{movie.title}- Fantastika janridagi film reytingi {movie.rating}"
    
movie = Movie("Harry Potter and the Sorcerer's Stone", "2h 32m", "Fantacy", 7.6 )
print(movie.show_summary())

