string_word="hello"
def convertCamel(string):
    res=''
    for i in string:
        if(i.isupper()):
            res+='_'+i.lower()
        else:
            res+=i
    return res[1:]
mystr="hello"
print(convertCamel(mystr))
    