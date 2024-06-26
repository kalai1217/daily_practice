arr=[1,2,3,0,4,5,0,6,7,0,0]
non_zero=[]
zero=[]
for i in range(0,len(arr)):
    if arr[i]!=0:
        non_zero.append(arr[i])
    else:
        zero.append(arr[i])
print(non_zero)
print(zero)
non_zero.extend(zero)
print(non_zero)