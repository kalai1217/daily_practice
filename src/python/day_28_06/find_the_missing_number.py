# Q2:
 
# list = [3,0,1,4,6,2,7,10]
 
# find the missing element in this list (0,1,2,3.....n)

# lst=[3,0,1,4,6,2,7,10]
# n=len(lst)
# miss=[]
# for i in range(n+1):
#     if i not in lst:
#         print(i)
lst = [3,0,1,4,6,2,7,10]
n = max(lst)
missing_numbers = []
for i in range(n+1):
    if i not in lst:
        missing_numbers.append(i)
print("Missing numbers:", missing_numbers)

