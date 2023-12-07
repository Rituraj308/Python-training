#scope - what variables do i have access to
def some_func():
    total = 100
    print(total)
#we get error because its inside of the function , it shows as the name total is not defined, This is because of the
#python's function scope. but if the same total is not inside the function then we can print because it global & we have
# access to it
# but if we use anything other than function like below code then we can print
if True:
    x=10
    print(x)