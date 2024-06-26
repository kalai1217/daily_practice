seq="This is a longest word abcndkdkdkgena;kd;lsd"
newseq=seq.split()
max=seq[0]
for i in newseq:
    if len(max) < len(i):
        max=i
print(max)
