list1=[1,5,2,3,7]
n=len(list1)
for i in range(0,n-2):
    min=i
    for j in range(i+1,n-1):
        if list1[min]>list1[j]:
            min=j
    temp=list1[i]
    list1[i]=list1[min]
    list1[min]=temp
print(list1)
