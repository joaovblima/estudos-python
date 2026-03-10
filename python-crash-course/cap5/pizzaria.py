recheios_disponiveis = ["cogumelo", " peperoni", "abacaxi",
                        "queijo extra"]
recheiros_solicitados = ["cogumelo", "banana nevada", "batata frita"]

for recheio_solicitado in recheiros_solicitados:
    if recheio_solicitado in recheios_disponiveis:
        print("adicionando", recheio_solicitado)
    else:
        print("infelizmente nao temos", recheio_solicitado, "disponivel")
