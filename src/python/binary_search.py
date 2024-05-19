n=int(input("Enter the no of elements"))
l2=[]
for i in range(n):
    l2.append(int(input("Enter elements")))
key=int(input("Enter key element"))
n=len(l2)
low=0
high=n-1
flag=0
while(low<=high):
    mid=(low+high)//2
    if (key==l2[mid]):
        flag=1
        break
    elif (key<l2[mid]):
        high=mid-1
    else:
        low=mid+1
if(flag==1):
    print("element found")
else:
    print("element not found")
