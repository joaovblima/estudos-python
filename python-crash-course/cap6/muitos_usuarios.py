usuarios = {
    "joao": {
        "nome": "joao",
        "sobrenome": "lima",
        "cidade": "uniao dos palmares",
    },
    "maria": {
        "nome": "maria",
        "sobrenome": "de melo lima",
        "cidade": "dragonstone",
    },
    "ingrid": {
        "nome": "ingrid",
        "sobrenome": "melo",
        "cidade": "braavos",
    },
}

for usuario, usuario_info in usuarios.items():
    print(usuario, "->", usuario_info)
