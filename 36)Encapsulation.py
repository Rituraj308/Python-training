#Encapsulation is the binding of data & fuctions that manipulate that data. And we encapsulate into one big objest so
# that we keep everything in this box that users or code or other machines can interact with.
class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
     print(f'my name is {self.name},and i am {self.age} years old.')

Player = PlayerCharacter('Ritu Raj', 25)
Player.speak()
