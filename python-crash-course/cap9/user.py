class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print("\nNome", "->", self.first_name.title())
        print("Sobrenome", "->", self.last_name.title())

    def greet_user(self):
        print("\nOla", self.first_name.title(), "boa tarde!")


joao = User("joao", "lima")
ingrid = User("ingrid", "melo")
maria = User("maria sofia", "de melo lima")

joao.describe_user()
ingrid.describe_user()
maria.describe_user()

joao.greet_user()
ingrid.greet_user()
maria.greet_user()
