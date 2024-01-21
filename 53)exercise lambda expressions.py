# square 1) creat a lambda expresion that square our list
my_list = [5, 4, 3]

print(list(map(lambda item : item**2, my_list)))

#List sorting
#we have to sort based on the 2nd number
a = [(0, 2), (4, 3), (10, -1), (9, 9)]
a.sort(key=lambda x:x[1])
print(a)