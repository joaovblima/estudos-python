import json


def get_new_numero_favorito():

    numero = input("Qual o seu numero favorito? ")
    filename = "numero_favorito.json"
    with open(filename, "w") as file_object:
        json.dump(numero, file_object)
        return numero


def get_numero_favorito():

    filename = "numero_favorito.json"
    try:
        with open(filename) as file_object:
            numero_favorito = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return numero_favorito


def numero_favorito_usuario():
    numero = get_numero_favorito()
    if numero:
        print("Seu numero favorito é: ", numero)
    else:
        numero = get_new_numero_favorito()
        print("O numero", numero, "foi salvo como seu favorito.")


numero_favorito_usuario()
