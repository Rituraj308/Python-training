a=10
def confusion (b):
    print(b)
    a=90

confusion(300)

total = 0
def count():
    global total
    total += 1
    return total
count()
count()
print(count())
# other way of doing the above func is by using dependency injection
total = 0
def count(total):
    total += 1
    return total
print(count(count(count(total))))
