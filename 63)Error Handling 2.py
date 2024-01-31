def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError:
        print('Please enter numbers')

print(sum(1,2))