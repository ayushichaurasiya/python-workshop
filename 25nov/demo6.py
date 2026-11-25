#function overriding
#same name  function in derived class
class base:
    def display (self):
     print("base class calles")
class derived:
    def display (self):
     base.display(self)
    #base class constructor
    super().__init__()
    print("derived class called")
    obj = derived()
    obj.display()
