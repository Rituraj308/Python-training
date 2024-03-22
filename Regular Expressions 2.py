import re    #re= regular expression

pattern = re.compile(r"([a-zA-Z]).([a])") #r is a raw string,it ignores everything that python interpreter might interpret
string = 'search this inside of this text please'

a=pattern.search(string)
print(a.group())
print(a.group(1))
print(a.group(2))