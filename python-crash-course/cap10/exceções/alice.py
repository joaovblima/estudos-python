

def count_words(filename):
    try:
        with open(filename) as file_obj:
            file = file_obj.read()
    except FileNotFoundError:
        msg = "Me desculpe mas o arquivo " + filename + " não foi encontrado"
        print(msg)

    else:
        palavras = file.split()
        num_palavras = len(palavras)
        print("o arquivo", arquivo + " contem " +
              str(num_palavras) + " palavras")


arquivo = "alice.txt"
count_words(arquivo)
