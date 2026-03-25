arquivo = "guest_book.txt"
continuar = True

while continuar:
    nome = input("Qual o seu nome? ")
    print("Saudações meu bom,", nome.title())
    with open(arquivo, "a") as file_object:
        file_object.write(nome + "\n")

    entrada = input("Deseja continuar? (s/n) ")
    if entrada == "s":
        continue
    else:
        continuar = False
