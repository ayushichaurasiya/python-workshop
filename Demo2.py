# Write a program to find maximum among 3 numbers using multiple if statements without elif.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Maximum =", a)

if b >= a and b >= c:
    print("Maximum =", b)

if c >= a and c >= b:
    print("Maximum =", c)