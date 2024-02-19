#Getters & Setters

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @property
    def title(self):
        print("getting title")
        return self._title

    @title.setter
    def title(self,value):
        print("setting title")
        self._title = value

    @title.deleter
    def title(self):
        del self._title

    def read_book(self):
        print("Reading", self.title, "by", self.author)

book1 = Book("Harry Potter", "JK Rowling");
# book1.title = "Half-Blood Prince"

print(book1.title)
book1.read_book()