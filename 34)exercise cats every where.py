class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

cat1 =Cat('cat1',5)
cat2 =Cat('cat2',7)
cat3 =Cat('cat3',4)

def oldest_cat(*args):
    return max(args)

print(f'oldest cat is {oldest_cat(cat1.age,cat2.age,cat3.age)} years old.')
