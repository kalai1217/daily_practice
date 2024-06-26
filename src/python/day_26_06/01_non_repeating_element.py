lst=[1,9,2,2,3,3,5,2,1,6,7,8]
freq={}
for i in lst:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
for i in freq:
    if freq[i]==1:
        print(i)
        break
print(freq)