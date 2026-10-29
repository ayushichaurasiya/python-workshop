res = 0
n = 153
temp = n
while(n!=0):
    a = n % 10
    res = (a**3) + res
    n = n // 10

if(temp==res):
    print("No. is armstrong")
else:
    print("No. is not an armstrong no.")