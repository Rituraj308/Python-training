# we use '_' to make a variable private in python .Although it doesn't give any special power to variable ,but as a
# python programmer we determine that if we see a '_' in the variable we should understand that it's a private variable
# and it should't be modified .
class PlayerCharacter:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def speak(self):
     print(f'my name is {self._name},and i am {self._age} years old.')

Player1 = PlayerCharacter('Ritu Raj', 25)
#Player1.name = '!!!'
#Player1.speak = 'BOOOO'

print(Player1.speak())