# Topic: Custom Classes in Python
class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}

# Example usage
rect = Rectangle(5, 10)

# Iterating over the Rectangle instance
for dimension in rect:
    print(dimension)

