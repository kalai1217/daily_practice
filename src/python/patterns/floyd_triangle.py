n=int(input('Enter the no of rows'))
c=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(c,end=' ')
        c+=1
    print()