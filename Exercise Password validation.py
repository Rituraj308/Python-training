#using Re creat a password checker
#it should be 8 char long
#it should contain any short of letters , nummbers and $%#@
#password has to end with a number

import re    #re= regular expression

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)") #r is a raw string,it ignores everything that python interpreter might interpret
string = 'rituraj'
pattern2 = re.compile(r"[A-Za-z0-9$%#@]{8,}\d")
password = 'fsdhfsnkjldglkdh2343%$9'

a=pattern.search(string)
check = pattern2.fullmatch(password)
print(check)
