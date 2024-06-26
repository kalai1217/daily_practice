# arr=[1,2,3,4,5]
# k=2
# k=k%len(arr)
# l,r=0,len(arr)-1
# while l<r:
#     arr[l],arr[r]=arr[r],arr[l]
#     l,r=l+1,r-1
# print(arr)

arr=[1,2,3,4,5]
n=len(arr)
d=3
d=d%n
temp=[]
for i in range(0,d):
    temp.append(arr[i])
print(temp)
for i in range(d,n):
    arr[i-d]=arr[i]
print(arr)
for i in range(n-d,n):
    arr[i]=temp[i-(n-d)]
print(arr)