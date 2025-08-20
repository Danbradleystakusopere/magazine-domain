

class Author:
    def __init__(self, name):
        
        if type(name) is not str or len(name) == 0:
            raise Exception("Name must be a non-empty string")
        self._name = name   

    @property
    def name(self):
        
        return self._name
