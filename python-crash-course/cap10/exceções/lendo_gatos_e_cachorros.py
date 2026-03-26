
def lendo_arquivos(arquivo):
    try:
        with open(arquivo) as file_object:
            nome = file_object.read()
            print(nome)
    except FileNotFoundError:
        pass
        # print("O arquivo " + arquivo + " não foi encontrado")


arquivos = ["gatos.txt", "cachorro.txt"]

for arquivo in arquivos:
    lendo_arquivos(arquivo)
