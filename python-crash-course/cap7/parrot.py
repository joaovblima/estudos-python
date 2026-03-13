prompt = "Tell me something, and i will repeat it back to you"
prompt += "\nEnter 'quit' to end the program. "

mensagem = ""
ativo = True

while ativo:
    mensagem = input(prompt)
    if mensagem == "quit":
        ativo = False
    else:
        print(mensagem)
