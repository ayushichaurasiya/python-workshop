def  demo():
    yield 10
    yield 20
    yield 30
x=demo()
print(next(x))  
print(next(x))   
print(next(x))   

for x in demo():
    print(x)