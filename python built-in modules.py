import random
print(random.random())
#it gives random numbers
print(random.randint(1,10)) #it gives random integers bw numbers
print(random.choice([1,2,3,4,6]))#it makes random choice and pick the number from the list
my_list = [1,2,3,4,5,6]
random.shuffle(my_list)
print(my_list)