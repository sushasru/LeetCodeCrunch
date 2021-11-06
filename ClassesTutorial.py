class Book():
    def __init__(self,title,author):
        self.title = title
        self.author = author
        print("Initialized")

    def __str__(self):
        return '"{}" by {}'.format(self.title,self.author)

class PaperBook(Book):
    def __init__(self,title,author,numPages):
        Book.__init__(self,title,author)
        self.numPages = numPages
        print("Initializing Paper Book")

class EBook(Book):
    def __init__(self,title,author,size):
        Book.__init__(self,title,author)
        self.size = size
        print("Initializing eBook")

class Library:
    def __init__(self):
        self.books = []
        print("Initializing Library")

    def addBook(self,book):
        self.books.append(book)
        print("Added book")

    def getNumBooks(self):
        print("Getting no. of books")
        return len(self.books)

myBk = EBook("The Odyssey","Homer",2)
myBk = EBook("Eleven Minutes","Paulo Coelho",2)
addl = Library()
addl.addBook(myBk)
print(addl.getNumBooks())
    
