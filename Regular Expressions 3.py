import re    #re= regular expression

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)") #r is a raw string,it ignores everything that python interpreter might interpret
string = 'b@b.com'
string2 = 'rituraj'
a=pattern.search(string)
b=pattern.search(string2)
print(a)
print(b)