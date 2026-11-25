#multiple inheritance
#multiple base classes and single derived class
class base1:
    def seta(self):
        self.a=100
        return(self.a)
class base2:
    def setb(self):
        self.b=200
        return(self.b)
class derived(base1,base2):
     def display(self):
        self.x=base1.seta(self)
        self.y=base2.setb(self)
        self.z=(self.x+self.y)/2
        print("z",self.z)
        obj=derived()
        obj.display()
