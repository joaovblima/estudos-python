class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attemps = 0

    def describe_user(self):
        print("\nNome", "->", self.first_name.title())
        print("Sobrenome", "->", self.last_name.title())

    def greet_user(self):
        print("\nOla", self.first_name.title(), "boa tarde!")

    def increment_login_attemps(self):
        self.login_attemps += 1

    def reset_login_attemps(self):
        self.login_attemps = 0
        print("as tentativas de login foram resetadas.")


joao = User("joao", "lima")
ingrid = User("ingrid", "melo")
maria = User("maria sofia", "de melo lima")

joao.increment_login_attemps()
print(
    "as tentativas de login de ", joao.first_name.title(), "foram", joao.login_attemps
)
joao.reset_login_attemps()
print(joao.first_name.title(), "tentativas de login:", joao.login_attemps)


# joao.describe_user()
# ingrid.describe_user()
# maria.describe_user()

# joao.greet_user()
# ingrid.greet_user()
# maria.greet_user()
