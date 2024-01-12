class Usser():
    def __init__(self, email):
        self.email = email

    def sign_in(self,email):
        print('logged in')


class Wizard(Usser):
   def __init__(self, name, power, email):
       super().__init__(email)
       self.name = name
       self.power = power

   def attack(self):
       print(f'attacking with power of {self.power}')


class Archer(Usser):
    def __init__(self, name, num_arrows, email):
        super().__init__(email)
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left- {self.num_arrows}')

wizard1 = Wizard('Merlin', 50, 'merlin@gmail.com')
archer1 = Archer('Robin', 100, 'robine@gmail.com')

print(wizard1.email)
print(archer1.email)
