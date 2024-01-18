# MAP allows us to simply our code , # MAP doesn't affect the outside world
my_list = [1,2,3]
def multiply_by2(li):
    return li*2


print(list(map(multiply_by2, my_list)))
print(my_list)