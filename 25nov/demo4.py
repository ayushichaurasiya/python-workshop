from abc import ABC,abstractmethod

class base(ABC):
    @abstractmethod
    def display(self):
        pass
    class derived(base):
        def display(self):
            print("display called in derived")
            def demo():
                print("demo called")
            obj=derived()
            obj.dispaly()
            obj.demo()