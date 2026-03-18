class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting")

    def roll_over(self):
        print(self.name.title() + " is rolled over")


meu_cachorro = Dog("mel", 9)
meu_cachorro.sit()
meu_cachorro.roll_over()
print("O nome do meu cachorro é " + meu_cachorro.name.title())
print(meu_cachorro.name.title() + " tem " +
      str(meu_cachorro.age) + " anos de idade")

seu_cachorro = Dog("pirulito", 12)
seu_cachorro.sit()
seu_cachorro.roll_over()

print("O nome do meu cachorro é " + seu_cachorro.name.title())
print(seu_cachorro.name.title() + " tem " +
      str(seu_cachorro.age) + " anos de idade")
