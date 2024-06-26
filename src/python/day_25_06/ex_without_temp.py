num=72
flag=True
for i in range(2,num):
    if(num%i!=0):
        flag=False
if flag==True:
    print("prime")
else:
    print("non prime")
        