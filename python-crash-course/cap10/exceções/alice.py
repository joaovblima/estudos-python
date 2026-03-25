arquivo = "alice.txt"

try:
    with open(arquivo) as file_obj:
        file = file_obj.read()
except FileNotFoundError:
    msg = "Me desculpe mas o arquivo " + arquivo + " não foi encontrado"
    print(msg)
