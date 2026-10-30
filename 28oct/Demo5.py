# Write a program to calculate profit and loss using cost price and selling price.

cp = float(input("Enter cost price: "))
sp = float(input("Enter selling price: "))

if sp > cp:
    profit = sp - cp
    print("Profit =", profit)

if cp > sp:
    loss = cp - sp
    print("Loss =", loss)

if cp == sp:
    print("No Profit No Loss")