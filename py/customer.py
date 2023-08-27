class Customer:

    #init method that takes two arguments
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        pass

    def given_name(self):
        return self.first_name
    
    def set_given_name(self, first_name):
        self.first_name = first_name

    def family_name(self):
        return self.last_name 
    
    def set_family_name(self, last_name):
        self.last_name = last_name

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
