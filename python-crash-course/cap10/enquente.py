arquivo = "resultado_da_enquete.txt"
continuar = True
while continuar:
    nome = input("Qual o seu nome? ")
    resposta = input("Porque você gosta de programar? ")
    with open(arquivo, "a") as file_object:
        file_object.write(nome + ", ")
        file_object.write(resposta+"\n")

    entrada = input("Deseja continuar? (s/n) ")
    if entrada == "s":
        continue
    else:
        continuar = False
