class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_read = False 

    def mark_as_read(self):
        self.is_read = True

    def status(self):
        if self.is_read:
            return f"{self.title} - O‘qilgan"
        else:
            return f"{self.title} - O‘qilmagan"



book1 = Book("Ufq", "Chingiz Aytmatov")
book2 = Book("Mehrobdan chayon", "Tog‘ay Murod")
book3 = Book("1984", "George Orwell")
book4 = Book("Alkimyogar", "Paulo Coelho")

book1.mark_as_read()
book3.mark_as_read()

books = [book1, book2, book3, book4]
for book in books:
    print(book.status())
