# In filter we can filter out some of our function , Filter function try to return a bollien value, it checks whether it
# it should be filtered or not .
my_list = [1,2,3]


def only_odd(li):
    return li % 2 != 0


print(list(filter(only_odd, my_list)))
print(my_list)