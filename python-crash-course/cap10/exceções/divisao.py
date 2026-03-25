print("Me de dois numeros e eu vou dividi-los")
print("Aperte q para sair")

while True:
    primeiro_numero = input("\nPrimeiro numero: ")
    if primeiro_numero == "q":
        break
    segundo_numero = input("Segundo numero: ")
    if segundo_numero == "q":
        break
    try:
        resposta = int(primeiro_numero)/int(segundo_numero)
    except ZeroDivisionError:
        print("Você não pode fazer uma divisão por zero")
    else:
        print(resposta)
