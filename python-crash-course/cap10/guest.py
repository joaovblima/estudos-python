nome = input("qual é o seu nome? ")

with open("teste-nome.txt", "w") as file_object:
    file_object.write(nome)
