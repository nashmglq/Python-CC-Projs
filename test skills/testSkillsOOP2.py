'''
Build a simple library system with books and users.
This exercise involves creating multiple classes, using inheritance, and demonstrating polymorphism.
'''

# Review of basic OOP

class Book:
    
    # Initialize the attributes
    def __init__(self, author, title, page, genre):
    #Provide a value for the self(object (class Book)) which will be used for the methods
        self.author = author
        self.page = page
        self.genre = genre
        self.title = title
        
    
    def frontPage(self):
        print(f"You are reading {self.title} by {self.title}")
    
    def endPage(self):
        print(f"This is a {self.genre} which contains {self.page} pages")
        
    

book1 = Book("F. Scott Fitzgerald", "The Great Gatsby", 180, "Novel")


book1.frontPage()
book1.endPage()