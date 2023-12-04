a='hellloooooooo'
if (len(a) > 10):
    print(f"too long {len(a)} elements")
#we r using 2 times 'len' in the code so to remove that we can use walrus opertor
a='hellloooooooo'
if ((n := len(a))>10):
    print(f"too long {n} elements")
while ((n := len(a))>1):
    print(n)
    a=a[:-1]
print(a)
