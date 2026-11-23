# Constructor is a special member function.
# In Python, constructor is defined by magic method __init__()

class product:

    # Parameterized constructor
    def __init__(self, qty, price):
        self.qty = qty
        self.price = price
        print("total =", (self.qty * self.price))

    def __del__(self):
        print("destructor called")


obj1 = product(3, 500)
obj2 = product(5, 1000)
obj3 = product(4, 2000)