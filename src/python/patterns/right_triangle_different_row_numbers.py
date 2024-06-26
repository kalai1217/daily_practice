#if you row values are different then always print j value in print statement
n=int(input("Enter the no of rows"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()
