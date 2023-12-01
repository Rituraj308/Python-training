#excersise = check for duplicates in list\
Some_list = ['a','b','c','b','d','m','n','n']

duplicates =[]
for value in Some_list:
    if Some_list.count(value)>1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)