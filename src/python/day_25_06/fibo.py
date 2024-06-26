num=int(input("Enter a number"))
n1=0
n2=1
sum=n1+n2
if num<=0:
    print("enter number greate than 0")
else:
    print(n1)
    print(n2)
    for i in range(2,num):
        print(sum)
        n1=n2
        n2=sum
        sum=n1+n2