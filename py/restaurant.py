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
        customer_list = ({r.customer for r in Review.all_reviews if r.restaurant.name == self._name})
        return customer_list

    # returns the average star rating for a restaurant based on its reviews
    def average_star_rating():
        pass

