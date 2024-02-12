# in this section we learned how to import function of one file to another file , for eg here we imorted utility function
#from uitlity.py file to main.py file and how to import a function from other directory/pythonpackg to other directory's file
import utility
import shopping.shopping_cart

print(utility.multiply(2,3))
print(shopping.shopping_cart.buy('apple'))
