from random import randint


class Dado:
    def __init__(self):
        self.lados = 6

    def rodar_dado(self):
        x = randint(1, self.lados)
        return x


dado = Dado()
print(dado.rodar_dado())

teste = randint(1, 6)
print(teste)
