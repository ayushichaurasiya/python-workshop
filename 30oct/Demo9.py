#nosted  for in loop
n=int(input("enter the limit"))
for i in range(1,4):
    #for space
    for k in range(3,i,-1):
     print(end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
        print()