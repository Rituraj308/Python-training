# *args & ** kwargs
def super_func(*args):
    print(*args)
    return sum(args)


super_func(1, 2, 3, 4, 5)


def super_func(*args):
    print(args)
    return sum(args)


super_func(1, 2, 3, 4, 5)


def super_func(*args):
    print(args)
    return sum(args)


print(super_func(1, 2, 3, 4, 5))


def super_func(*args, **kwargs):
    print(kwargs)
    return sum(args)


print(super_func(1, 2, 3, 4, 5, num1=5, num2=10))


def super_func(*args, **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args)+total


print(super_func(1, 2, 3, 4, 5, num1=5, num2=10))
