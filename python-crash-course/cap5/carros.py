carros = ['audi', 'bmw', 'subaru', 'toyota']
for carro in carros:
    if carro == 'bmw':
        print(carro.upper())
    elif carro == "subaru":
        print("carro == subaru? Eu acho que sim")
    elif carro == "audi":
        print("carro == audi? Eu acho que nao")
    else:
        print(carro.title())
