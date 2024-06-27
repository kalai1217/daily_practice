def add(x,y):
    while(y!=0):
        carry=x&y
        x=x^y
        y=carry<<1
    return x
print(add(5,2))