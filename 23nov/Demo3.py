x=10 #global variable
print("outside functoin x=",x)
def demo():
    global y
    y=20 #local variable
    print("inside function x=",x)
    print("inside function y=",y)

    demo()