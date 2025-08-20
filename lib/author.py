from lib.article import Article
from lib.magazine import Magazine

class Author:
    def __init__(self, name):
        if type(name) is not str or len(name) == 0:
            raise Exception("Name must be a non-empty string")
        self._name = name

    @property
    def name(self):
        return self._name

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    
    def add_article(self, magazine, title):
        if not isinstance(magazine, Magazine):
            raise Exception("Must pass a Magazine instance")
        return Article(self, magazine, title)

    
    def topic_areas(self):
        if len(self.articles()) == 0:
            return None
        return list({magazine.category for magazine in self.magazines()})
