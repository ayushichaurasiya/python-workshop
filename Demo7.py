#prg for print div on the basis of percentage
per=float(input("enter your percentage: "))
if(per>=60):
    print("I div.")
elif(per>=45 and per<60):
    print("II div.")
elif(per>=30 and per<45):
    print("III div.")
else:
    print("fail")