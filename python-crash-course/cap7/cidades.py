prompt = "Entre com o nome da cidade que voce visitou: "
prompt += "\n(Escreva 'sair' quando voce acabar) "

while True:
    cidade = input(prompt)
    if cidade == "sair":
        break
    else:
        print("Que bela cidade eh", cidade.title(), "foi uma otima escolha")
