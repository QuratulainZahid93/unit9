class User():
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()

    def describe_user(self):
        """Display a summary of the user's information."""
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print("\nWelcome back, " + self.username + "!")

QuratulainZahid = User('Quratulain','Zahid','QuratulainZahid', 'quratulain@example.com', 'Pakistan')
QuratulainZahid.describe_user()
QuratulainZahid.greet_user()

Samar = User('Samar', 'Sadique', 'SamarSadique', 'wb@example.com', 'Pakistan')
Samar.describe_user()
Samar.greet_user()