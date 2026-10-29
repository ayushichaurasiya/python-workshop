# Write a program to reverse a 3-digit integer (num = 236).

num = 236

a = num % 10
b = (num // 10) % 10
c = num // 100

rev = a * 100 + b * 10 + c

print("Reverse =", rev)