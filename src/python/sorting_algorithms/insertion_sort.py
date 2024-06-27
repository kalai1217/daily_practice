arr=[7,3,8,2,1]
n=len(arr)
for i in range(1,n):
    temp=arr[i]
    # for j in range(i,0 and temp>arr[j-1],-1):
    j=i
    while j>0 and temp<arr[j-1]:
        arr[j]=arr[j-1]
        j-=1
    arr[j]=temp
print(arr)
