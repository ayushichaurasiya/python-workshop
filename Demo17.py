# Leap year check
yr = int(input("Enter any year: "))

if(yr%400==0 or yr%4==0):
    print("Leap year")
else:
    print("Not a leap year")