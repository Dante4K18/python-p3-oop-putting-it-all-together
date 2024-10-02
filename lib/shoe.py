class Shoe:
    def __init__(self, brand: str, size: float, color: str):
        self.brand = brand
        self.size = size
        self.color = color

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value: str):
        if isinstance(value, str) and len(value) > 0:
            self._brand = value
        else:
            raise ValueError("Brand must be a non-empty string.")

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value: float):
        if isinstance(value, (int, float)) and value > 0:
            self._size = value
        else:
            raise ValueError("Size must be a positive number.")

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value: str):
        if isinstance(value, str) and len(value) > 0:
            self._color = value
        else:
            raise ValueError("Color must be a non-empty string.")

    def __str__(self):
        return f"{self.brand} shoe, size {self.size}, color {self.color}"
