from review import Review

class Customer:

    all_customers = []

    #init method that takes two arguments
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        Customer.all_customers.append(self)

    # return the customer given name (first name) 
    @property
    def given_name(self):
        return self.first_name
    
    @given_name.setter
    def given_name(self, first_name):
        self.first_name = first_name

    # return the customer family name (last name)
    @property
    def family_name(self):
        return self.last_name 
    
    @family_name.setter
    def family_name(self, last_name):
        self.last_name = last_name

    # returns the full name of the customer 
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    # returns all of the customers 
    @classmethod
    def all(cls):
        return cls.all_customers

    # returns a unique list of all restaurants a customer has reviewed
    def restaurants(self):
        restaurant_list = ({r.restaurant for r in Review.all_reviews if r.customer.full_name == self.full_name})
        return restaurant_list

    # creates a new review and associates it with that customer and restaurant
    def add_review(self, restaurant, rating):
        Review(self, restaurant=restaurant, rating=rating)

    # returns the total number of reviews that a customer has authored
    def num_reviews(self): 
        rev = Review.all_reviews
        return len([r for r in rev if r.customer.full_name == self.full_name])
    
    # given a string of a full name returns the first customer whose full name matches 
    def find_by_name(cls, name):
        for customer in cls.all_customers:
            if customer.full_name == name:
                return customer

    # given a string of a given name returns a list containing all customers with that given name
    def find_all_by_given_name(cls, name):
        for customer in cls.all_customers:
            if customer.given_name == name:
                return customer