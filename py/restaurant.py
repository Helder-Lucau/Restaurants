from review import Review

class Restaurant(Review):

    # init method that takes one argument
    def __init__(self, name):
        self._name = name
    
    # returns the restaurant's name
    def name(self):
        return self._name
    
    # returns a list of all reviews for that restaurant
    def reviews(self):
        rev = Review.all_reviews
        return [r for r in rev if r.restaurant.name == self._name]

    # returns a unique list of all customers who have reviewed a particular
    def customers(self):
        return 

    def average_star_rating():
        pass
    