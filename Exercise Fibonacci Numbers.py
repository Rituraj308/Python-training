# fibonaacci numbers- we add the 1st 2 numbers to get the 3rd number
#using generator method
def fib(numbers):
    a=0
    b=1
    for i in range(numbers):
        yield a
        temp = a
        a = b
        b = temp + b

for x in fib(21):
    print(x)
#using list method
def fib2(numbers):
    a=0
    b=1
    result = []
    for i in range(numbers):
        result.append(a)
        temp = a
        a = b
        b = temp + b
    return result
print(fib2(10))
