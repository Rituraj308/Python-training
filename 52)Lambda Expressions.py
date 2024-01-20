#Lambda functions are similar to user-defined functions but without a name. They're commonly referred to as
# anonymous functions. Lambda functions are efficient whenever you want to create a function that will only contain
# simple expressions – that is, expressions that are usually a single line of a statement. and it can be used only once
my_list = [1,2,3]



print(list(map(lambda item: item*2, my_list)))
print(list(filter(lambda item: item%2 !=0, my_list)))
