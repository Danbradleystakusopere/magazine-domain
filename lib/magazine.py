

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
