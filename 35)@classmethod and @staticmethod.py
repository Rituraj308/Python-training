class PlayerCharacter:
    #class object attribute
    membership = True
    def __init__(self,name,age):
        if(self.membership):
            self.name = name
            self.age = age
    def shout(self):
        print(f'my name is {self.name}')
    @classmethod
    def adding_things(cls,num1, num2):
        return num1 + num2


player1 = PlayerCharacter('Cindy', 22)

print(player1.adding_things(2,3))
      #or we can do in this way also
class PlayerCharacter:
    #class object attribute
    membership = True
    def __init__(self,name,age):
        if(self.membership):
            self.name = name
            self.age = age
    def shout(self):
        print(f'my name is {self.name}')
    @classmethod
    def adding_things(cls,num1, num2):
        return num1 + num2


#player1 = PlayerCharacter('Cindy', 22)

print(PlayerCharacter.adding_things(2,3))