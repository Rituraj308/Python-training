# Decorator supercharges our function & add extra function

def my_decorator(func):
    def wrap_func():
        print('*******')
        func()
        print('*******')
    return wrap_func

@my_decorator
def hello():
    print('helloooo')
@my_decorator
def bye():
    print('seee yaaa laterr')
hello()
bye()