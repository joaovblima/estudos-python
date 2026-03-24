arquivo = "dados_eleitorais.txt"
dict_info = {}
with open(arquivo) as f_o:
    informacoes = f_o.read()
    print(informacoes)
