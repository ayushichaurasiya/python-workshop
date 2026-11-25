
# Operator Overloading

class number:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return (x, y)

obj1 = number(10, 20)
obj2 = number(20, 30)

obj3 = obj1 + obj2  # call __add__()

print("Addition =", obj3)
