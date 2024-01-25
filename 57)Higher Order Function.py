#HOC can be one of two things . it could either be a function that accepts another function or another way is if its a
#a function that returns another function.
def greet(func):
    func()

#another way
def greet2():
    def func():
        return 5
    return func
#map(), reduce() & filter() are also higher order function