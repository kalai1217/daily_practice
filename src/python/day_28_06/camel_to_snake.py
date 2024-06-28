def camel_to_snake(str):
    res=""
    for i in str:
        if(i.isupper()):
            res+="_"+i.lower()
        else:
            res+=i
    return res[1:]
str = "CamelCase"
print(camel_to_snake(str))