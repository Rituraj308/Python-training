class PlayerCharacter:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def run(self):
        print('run')
        return 'done'

player1 = PlayerCharacter('Cindy', 22)
player2 = PlayerCharacter('Tom', 34)
player2.attack = 50
print(player1.name)
print(player2.run())