lst=[1,2,3,4]
iterable=iter(lst)
print(iterable)
# for i in iterable:
#     print(i)
print(next(iterable))
try:
    print(next(iterable))
except StopIteration:
    print("iterator is empty")