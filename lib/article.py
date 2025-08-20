from lib.author import Author
from lib.magazine import Magazine

class Article:
    all = []  

    def __init__(self, author, magazine, title):
        if type(title) is not str or len(title) < 5 or len(title) > 50:
            raise Exception("Title must be a string between 5 and 50 characters")

        if not isinstance(author, Author):
            raise Exception("Author must be an instance of Author")

        if not isinstance(magazine, Magazine):
            raise Exception("Magazine must be an instance of Magazine")

        self._title = title
        self._author = author
        self._magazine = magazine

        Article.all.append(self)  
    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine
