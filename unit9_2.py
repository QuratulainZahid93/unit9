class Restaurant():
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = self.name + " serves wonderful " + self.cuisine_type + "."
        print("\n" + msg)

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = self.name + " is open. Come on in!"
        print("\n" + msg)

mean_queen = Restaurant('Student Pizza', 'pizza')
mean_queen.describe_restaurant()

ludvigs = Restaurant("Kolachi Karachi", 'seafood')
ludvigs.describe_restaurant()

mango_thai = Restaurant('Mango Thai', 'thai food')
mango_thai.describe_restaurant()