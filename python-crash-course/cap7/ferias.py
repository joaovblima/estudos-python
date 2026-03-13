prompt = "Se pudesse visitar um lugar do mundo, para onde você iria? "

resultado = {}
pesquisa_ativa = True
while pesquisa_ativa:
    nome = input("Qual o seu nome? ")
    lugar = input(prompt)
    resultado[nome] = lugar
    repetir = input("Gostaria de continuar a pesquisa? (sim/nao) ")
    if repetir == "nao":
        pesquisa_ativa = False

for nome, lugar in resultado.items():
    print(nome.title(), "gostaria de viajar para", lugar.title())
