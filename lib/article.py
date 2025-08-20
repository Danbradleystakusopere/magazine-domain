class Article:
    all = []

    def __init__(self, author, magazine, title):
        if type(title) is not str or not (5 <= len(title) <= 50):
            raise Exception("Title must be a string between 5 and 50 characters")

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
