from review import Review

class Restaurant(Review):

    # init method that takes one argument
    def __init__(self, name):
        self._name = name
    
    def name(self):
        return self._name
    
    def reviews(self):
        pass

    def customers(self):
        pass