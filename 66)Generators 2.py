def generator_function(num):
    for i in range(num):
        yield i                                  # yield pauses the function and starts again when its told to start and
                                                      # gives function one by one.it keeps on looping over &over till the end
for item in generator_function(1000):
    print(item)
# we just put only one item in memory. so in this way it uses less space in the memory

def generator_function(num):
    for i in range(num):
        yield i*2

g = generator_function(100)
next(g)
next(g)
print(next(g))
