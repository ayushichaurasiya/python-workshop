n = int(input("Enter any number: "))
temp = n
res = 0

while(n != 0):
    a = n % 10
    res = (res * 10) + a
    n = n // 10

print("Reversed no.: ", res)