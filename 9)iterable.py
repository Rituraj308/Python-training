# Iterables :- Iterable simply means it is an  object or a collection that can be iterated over
# itrtable cna be a list, dictionary, tuple, set or sting.
#iterate- one by one check each item im collection.
user = {
    'name' : 'Golem',
    'age' : 2020,
    'can_swim' : False
}
for item in user:
    print(item)
for item in user.items():
    print(item)
for item in user.values():
    print(item)
for item in user.keys():
    print(item)
for key,value in user.items():
    print(key,value)