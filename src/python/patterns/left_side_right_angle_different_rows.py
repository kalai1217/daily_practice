n=int(input("Enter the no of rows"))
for i in range(1,n+1):
    for s in range(1,n-i+1):
        print(' ',end=' ')
    for j in range(1,i+1):
        print(i,end=' ')
    print()
for i in range(n-1,-1,-1):
    for s in range(1,n-i+1):
        print(' ',end=' ')
    for j in range(1,i+1):
        print(i,end=' ')
    print()