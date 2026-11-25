#function overriding
#same name  function in base+derived class
class base:
    def display(self):
        print("base class calles")
        class derived:
            def display(self):
                base.display(self)#function within function
                print("derived class called")
                obj=derived()
                obj.display()
