pesquisa_de_montanha = {}
pesquisa_ativa = True

while pesquisa_ativa:
    nome = input("Qual eh o seu nome? ")
    montanha = input("Qual a montanha voce vai subir hoje? ")
    pesquisa_de_montanha[nome] = montanha
    repetir = input("Voce gostaria que outra pessoa respondesse? (sim/nao) ")
    if repetir == "nao":
        pesquisa_ativa = False


for nome, montanha in pesquisa_de_montanha.items():
    print(nome.title(), "gostaria de subir", montanha.title())
