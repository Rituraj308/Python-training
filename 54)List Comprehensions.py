#comprehension helps us to quickly  create lists or sets or dictionary in Python instead of perhaps looping or appending
# to a bunch of items to list
# formate for the code is my_list = [param for param in iterable]

my_list = [char for char in 'hello']
print(my_list)
#creat a list of nummbers reanging from 0 to 100
my_list2 = [num for num in range(0, 100)]
print(my_list2)
#creat a list of nummbers reanging from 0 to 100 but all the nums should be multiplied by 2
my_list3 = [num*2 for num in range(0, 100)]
print(my_list3)
# creat a list with power of 2 and print only even nums
my_list4 = [num**2 for num in range(0, 100) if num % 2 ==0]
print(my_list4)