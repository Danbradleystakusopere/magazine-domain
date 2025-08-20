from lib.article import Article
from lib.author import Author

class Magazine:
    def __init__(self, name, category):
        if type(name) is not str or len(name) < 2 or len(name) > 16:
            raise Exception("Name must be a string between 2 and 16 characters")

        if type(category) is not str or len(category) == 0:
            raise Exception("Category must be a non-empty string")

        self._name = name
        self._category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if type(new_name) is str and 2 <= len(new_name) <= 16:
            self._name = new_name
        else:
            raise Exception("Name must be a string between 2 and 16 characters")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if type(new_category) is str and len(new_category) > 0:
            self._category = new_category
        else:
            raise Exception("Category must be a non-empty string")

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})
    
    def article_titles(self):
        if len(self.articles()) == 0:
            return None
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        if len(self.articles()) == 0:
            return None
        authors = [article.author for article in self.articles()]
        return [author for author in set(authors) if authors.count(author) > 2] or None
    
    @classmethod
    def top_publisher(cls):
        if len(Article.all) == 0:
            return None
        return max(
            set([article.magazine for article in Article.all]),
            key=lambda mag: len(mag.articles())
        )
