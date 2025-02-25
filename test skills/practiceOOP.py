#Design a Library Management System using Object-Oriented Programming.
running = False



class Library:
    book = []
    
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        
    @classmethod
    def addBook(cls, title, author, ISBN):
        cls.books.append(title)
        
    def book(self):
        print(f"Title of Book: {self.title}\nAuthor: {self.author}\nISBN: {self.ISBN}")
    
    
    
    
class Members:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        
    
        
book1 = Library("The Catcher in the Rye", "J.D. Salinger", "978-0-316-76948-0")
book1.book()