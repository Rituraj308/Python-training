def sum(num1,num2):
    print('hiii')
    num1+num2
    return num1+num2
  # should do one thing relly well
  # should return something

print(sum(10,5))
totall = sum(10,5)
print(sum(10,totall))


def sum(num1,num2):
    def another_func(num1,num2):
        return num1+num2
    return another_func(num1,num2)

totall=sum(10,20)
print(totall)