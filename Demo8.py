#prg for airthmetic operation
print("press 1 for sum")
print("press 2 for sub")
print("press 3 for mul")
print("press 4 for div")
ch=int(input("choice"))
a=int(input("enter first no."))
b=int(input("enter second no."))
if(ch==1):
    c=a+b
    print("sum=",c)
elif(ch==2):
    c=a-b
    print("sub",c)
elif(ch==3):
    c=a*b
    print("mul",c)
elif(ch==4):
    c=a/b
    print("div",c)
else:
    print("invalid choice")

