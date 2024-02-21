#add print(__name__) in bothe utility.py and shopping cart.py
from utility import multiply, divide
from shopping.more_shopping import shopping_cart

print(shopping_cart.buy('apple'))
print(multiply(5,2))
print(divide(5,2))
print(max([1,2,3]))

#print(__name__)
if __name__ == '__main__':
    print('please run this')