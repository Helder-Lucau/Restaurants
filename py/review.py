class Review:

    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self._customer = customer
        self._restaurant = restaurant
        self.rating = rating
        Review.all_reviews.append(self)
    
    # returns the rating for a restaurant 
    @property
    def rating(self):  
        return self.rating  
    
    # returns all of the reviews
    @classmethod
    def all(cls):
        return cls.all_reviews
    
    # returns the customer object for that review
    @property
    def customer(self):
        return self._customer
    
    # returns the restaurant object for that given review
    @property
    def restaurant(self):
        return self._restaurant

    
    

