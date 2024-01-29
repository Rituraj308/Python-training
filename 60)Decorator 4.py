#why do we need decorators?
#creating a performance decorator to see how long a particular code takes time to run
from time import time
def performance(fn):
    def wrapper(*args,**kwargs):
        t1 = time()
        result= fn(*args,**kwargs)
        t2 = time()
        print(f'took{t2-t1} ms')
        return result
    return wrapper()
@performance
def long_time():
    for i in range(10000000):
        i*5

long_time()