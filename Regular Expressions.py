import re    #re= regular expression

pattern = re.compile('this')
string = 'search this inside of this text please'
print(re.search('this', string))
a=re.search('this', string)
print(a.span()) #it tells where the string occurs
print(a.start())#it tells where the text starts
print(a.end())#it tells where the text ends
print(a.group())#it returns the part of the string where this was the match
a=pattern.search(string)
b=pattern.findall(string) #it find all the instances of the match
c=pattern.fullmatch(string)
print(a.group())
print(b)
print(c)
