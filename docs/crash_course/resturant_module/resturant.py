"""
The resturant module exposes the Resturant class, that creates
resturant instances.
"""
class Resturant:
    """An attempt to model a Resturant."""
    # Sets the standard attributes to it's instances
    def __init__(self, resturant_name, cuisine_type):
        self.resturant_name = resturant_name
        self.cuisine_type = cuisine_type
        self.numbers_served = 0

    # A method that describes the resturant
    def describe_resturant(self):
        print(f"Name: {self.resturant_name}\nCuisine: {self.cuisine_type}")

    # A method that opens the resturant
    def open_resturant(self):
        print(f'The resturant: "{self.resturant_name}" is now open!')
    
    def set_number_served(self, value):
        self.numbers_served = value
    
    def increment_number_served(self, value):
        self.numbers_served = self.numbers_served + value

class IceCreamStand(Resturant):
    """An attemt to model an Ice Cream Stand type resturant."""
    def __init__(self, resturant_name, cuisine_type):
        super().__init__(resturant_name, cuisine_type)
        self.flavors = ["Chocolate", "Licorice", "Strawberry"]
    
    
    def get_flavors(self):
        print(self.flavors)