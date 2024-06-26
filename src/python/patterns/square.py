#printing square pattern
#for printing patterns we generally require two nested for loops
#outer and inner loop
#outer loop for no of rows and inner loop for columns
#if the row value is changing then we should print values in inner loop
#if the row value is constant then we should print values in outer loop
n=int(input("Enter the no of rows"))
for i in range(n):
    for j in range(n):
        print('*',end=' ')
    print()