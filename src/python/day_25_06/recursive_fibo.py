def recursiveFibo(n):
    if (n==0):
        return 0
    elif (n==1):
        return 1
    else:
        return (recursiveFibo(n-1)+recursiveFibo(n-2))   
n=7
for i in range(n):
    print(recursiveFibo(i))
    