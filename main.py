# in this section we learned how to import function of one file to another file , for eg here we imorted utility function
#from uitlity.py file to main.py file and how to import a function from other directory/pythonpackg to other directory's file
from utility import multiply, divide
from shopping.more_shopping.shopping_cart import buy

print(multiply(5,2))
print(divide(5,2))
print(buy('apple'))
