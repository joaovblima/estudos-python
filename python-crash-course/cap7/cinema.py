prompt = "Cinema draculino, boa noite. Qual a sua idade? "
ativo = True

while ativo:
    idade = input(prompt)
    if idade == "":
        ativo = False
    else:
        if int(idade) < 3:
            print("Ingresso gratuito.")
        elif int(idade) <= 12:
            print("Ingresso custa R$ 10,00")
        elif int(idade) > 12:
            print("Ingresso custa R$ 15,00")
