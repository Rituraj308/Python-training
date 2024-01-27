def my_decorator(func):
    def wrap_func(x,y):
        print('*******')
        func(x,y)
        print('*******')
    return wrap_func

@my_decorator
def hello(greetings, emoji):
    print(greetings, emoji)

hello('hiii', ':)')
 # or
def my_decorator2(func):
    def wrap_func2(*args, **kwargs):
        print('*******')
        func(*args, **kwargs)
        print('*******')
    return wrap_func2


@my_decorator2
def hello(greetings, emoji=':('): 
    print(greetings, emoji)

hello('hiiiii')