class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value: str):
        if isinstance(value, str) and len(value) > 0:
            self._title = value
        else:
            raise ValueError("Title must be a non-empty string.")

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value: str):
        if isinstance(value, str) and len(value) > 0:
            self._author = value
        else:
            raise ValueError("Author must be a non-empty string.")

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value: int):
        if isinstance(value, int) and value > 0:
            self._pages = value
        else:
            raise ValueError("Pages must be a positive integer.")

    def __str__(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages"
