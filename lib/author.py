

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
