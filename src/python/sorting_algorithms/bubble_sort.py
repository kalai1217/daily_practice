n=int(input("Enter the number of elements"))
l2=[]
for i in range(n):
    l2.append(int(input(f"Enter element {i}")))
print(l2)
for i in range(0,n-1):
    for j in range(0,n-i-1):
        if l2[j]>l2[j+1]:
            temp=l2[j]
            l2[j]=l2[j+1]
            l2[j+1]=temp
print(l2)
