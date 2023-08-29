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

    # return all of the customer 
    @classmethod
    def all(cls):
        return cls.all_customers

    def restaurants():
        pass

    def add_review(restaurant, rating):
        pass

    def num_reviews(): 
        pass

    def find_by_name(cls, name):
        for customer in cls.all_customers:
            if customer.full_name == name:
                return customer

    def find_all_by_given_name(cls, name):
        for customer in cls.all_customers:
            if customer.given_name == name:
                return customer