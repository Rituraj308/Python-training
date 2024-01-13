#Create a super list using the class super list.

class SuperList(list):
    def __len__(self): #let it be any length but it should always return 1000
        return 1000


super_list1 = SuperList()

print(len(super_list1))
super_list1.append(5)    # adding 5 to the start of the list
print(super_list1[0])
print(issubclass(SuperList, list)) #is Superlist a sub class of list.
print(issubclass(list, object))# is list a sub class of the base object.