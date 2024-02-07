from time import time
def perfromance(fn):
    def wrapper(*args,**kwargs):
        t1 = time()
        result = fn(*args,**kwargs)
        t2 = time()
        print(f'took {t2-t1}s')
        return result
    return wrapper()

@perfromance
def long_time():
    print('1')
    for i in range(100000000):
        i*5

@perfromance
def long_time2():
    print('2')
    for i in list(range(100000000)):                              #list takes longer time
        i*5

long_time()
long_time2()