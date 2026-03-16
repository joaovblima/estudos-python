def fazer_carro(nome_fabricante, modelo, **carro_infos):
    carro = {}
    carro["nome_fabricante"] = nome_fabricante
    carro["modelo"] = modelo
    for chave, valor in carro_infos.items():
        carro[chave] = valor

    return carro


carro_1 = fazer_carro("subaru", "outback", cor="preto", ano_fabricacao=2025)
carro_2 = fazer_carro("volksvagen", "nivus", cor="preto",
                      ano_fabricacao=2019, aro=22)
carro_3 = fazer_carro("toyota", "hilux")
print(carro_1)
print(carro_2)
print(carro_3)
