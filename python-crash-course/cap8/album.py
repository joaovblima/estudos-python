def make_album(nome_artista, titulo_album, numero_faixas=""):
    dict = {}
    if numero_faixas:
        dict[nome_artista] = titulo_album
        dict["numero_faixas"] = numero_faixas
    else:
        dict[nome_artista] = titulo_album
    return dict


while True:
    print("Nome do artista: ")
    print("Escreva 'q' para encerrar o programa a qualquer momento.")
    nome_do_artista = input()
    if nome_do_artista == 'q':
        break
    print("Nome do almbum: ")
    nome_album = input()
    if nome_album == 'q':
        break

    artista = make_album(nome_do_artista, nome_album)
    print(artista)
