class Product:
    def setdata(self, id, name, quantity, price):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price

    def display(self):
        print("Product ID:", self.id)
        print("Product Name:", self.name)
        print("Quantity:", self.quantity)
        print("Price:", self.price)


obj1 = Product()
obj1.setdata(101, "printer", 2, 20000)
obj1.display()