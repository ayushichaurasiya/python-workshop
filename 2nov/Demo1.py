
print("----- MENU -----")
print("1. Area of Circle")
print("2. Area of Rectangle")
print("3. Area of Square")
print("4. Area of Triangle")

choice = int(input("Enter your choice: "))

if choice == 1:
    r = float(input("Enter radius: "))
    area = 3.14 * r * r
    print("Area of Circle =", area)

elif choice == 2:
    l = float(input("Enter length: "))
    b = float(input("Enter breadth: "))
    area = l * b
    print("Area of Rectangle =", area)

elif choice == 3:
    s = float(input("Enter side: "))
    area = s * s
    print("Area of Square =", area)

elif choice == 4:
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    area = 0.5 * base * height
    print("Area of Triangle =", area)

else:
    print("Invalid Choice")
