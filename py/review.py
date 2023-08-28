class Review:

    reviews = []

    def __init__(self, customer, restaurant, rating):
        self._customer = customer
        self._restaurant = restaurant
        self.rating = rating
    
    # returns the rating for a restaurant
    def rating(self):  
        return self.rating  
    
    # returns the customer object for that review
    def customer(self):
        return self._customer
    
    # returns the restaurant object for that given review
    def restaurant(self):
        return self._restaurant

    # returns all of the reviews
    @classmethod
    def all(cls):
        return cls.reviews

