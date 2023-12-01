# check if even or odd
def is_even(num):
    if num % 2 == 0:
        return True
    elif num % 2 != 0:
        return False


print(is_even(50))
print(is_even(51))
# we can keep the code more clean and small if we are only checking for even


def is_even(num):
    if num % 2 == 0:
        return True
    return False


print(is_even(50))
# we can keepit more clean


def is_even(num):
    return num % 2 == 0


print(is_even(50))

