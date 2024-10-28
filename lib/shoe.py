class Shoe:
    def __init__(self, brand, size, color=None):
        self.brand = brand
        self.color = color
        self._size = None  # Use a private variable to store the size
        self.size = size  # Use the property setter to validate
        self.condition = "Used"  # Initialize condition to "Used"

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        else:
            self._size = value  # Set the value if it's an integer

    def cobble(self):
        """Simulate cobbling the shoe."""
        self.condition = "New"  # Set condition to "New"
        print("Your shoe is as good as new!")
