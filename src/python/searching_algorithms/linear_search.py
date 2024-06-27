n=int(input("Enter no of elements"))
flag=0
l1=[]
for i in range(n):
    l1.append(int(input("Enter elements")))
key=int(input("Enter key element"))
for i in range(0,n):
    if(l1[i]==key):
        flag=1
if(flag==1):
    print("Element found")
else:
    print("Element Not found")
