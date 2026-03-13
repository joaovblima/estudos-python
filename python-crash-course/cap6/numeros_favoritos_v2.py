numeros_favoritos = {
    "joao": [9, 99],
    "ingrid": [8],
    "maria sofia": [12, 22],
    "maria alice": [15, 33],
}

for nome, num_favorito in numeros_favoritos.items():
    print("Os numeros favoritos de", nome, "sao: ")
    for num in num_favorito:
        print(num)
