# Write a program to find the middle among 3 numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if (a >= b and a <= c) or (a <= b and a >= c):
    print("Middle =", a)

if (b >= a and b <= c) or (b <= a and b >= c):
    print("Middle =", b)

if (c >= a and c <= b) or (c <= a and c >= b):
    print("Middle =", c)