class Book:
    def __init__(self, title, author, is_read=False) -> None:
        self.title = title
        self.author = author
        self.is_read = is_read
    
    def status(self) -> None:
        if self.is_read:
            print("o'qilgan")
        else:
            print("o'qilmagan")
    
    def mark_as_read(self):
        self.is_read = True


b = Book('o\'tgan kunlar', 'Abdulla Qodiriy')
b.mark_as_read()
b.status()