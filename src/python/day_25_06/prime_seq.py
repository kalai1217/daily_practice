low=5
high=100
for num in range(low,high+1):
    for i in range(2,num):
        if num%i==0:
            break
    else:
        print(num)