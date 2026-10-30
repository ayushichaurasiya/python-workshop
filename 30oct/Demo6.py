#prg. for check given no. is prime no.or not

n = int(input("Enter any number: "))

found = 0  # Prime number

for i in range(2, n):
    if (n % i == 0):
        found = 1  # Not a prime number
        break

if (found == 1):
    print("Not a prime number")
else:
    print("Prime number")
