from collections import Counter,defaultdict,OrderedDict
li = [1,2,3,4,5,6,7,7]
sentence = 'bla bla i am using python'
print(Counter(li))
print(Counter(sentence))

dictionary = defaultdict(int,{'a': 1, 'b': 2})               #defaultdict allows u to call object which is not event present in the dict.
print(dictionary['c'])
dictionary2 = defaultdict(lambda : 'does not exists', {'a': 1, 'b': 2})
print(dictionary2['c'])

d = OrderedDict()                                    #OrderDict retains the order that u insert
d['b'] = 2
d['a'] = 1

d2 = OrderedDict()
d2['a'] = 1
d2['b'] = 2

print(d2 == d)