prompt = "Boa noite. Apresente os ingredientes que voce quer que sejam adicionados a pizza. "
prompt += "\n(Entre com 'sair' para encerrar o programa) "

ingrediente = ""
while True:
    ingrediente = input(prompt)
    if ingrediente == "sair":
        break
    else:
        print(ingrediente.title(), "foi adicionado a pizza.\n")
