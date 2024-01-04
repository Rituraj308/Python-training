class PlayerCharacter:
    #class object attribute
    membership = True
    def __init__(self,name,age):
        if(self.membership):
            self.name = name
            self.age = age
    def shout(self):
        print(f'my name is {self.name}')

player1 = PlayerCharacter('Cindy', 22)
player2 = PlayerCharacter('Tom', 34)
#player2.attack = 50
print(player1.shout())
print(player2.name)