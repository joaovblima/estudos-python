cidades = {
    "uniao dos palmares": {
        "pais": "brasil",
        "populacao": 60000,
        "fato": "cidade conhecida por terra de zumbi dos palmares",
    },
    "maceio": {
        "pais": "brasil",
        "populacao": 995000,
        "fato": "conhecida por ter uma belissica orla, uma das mais bonitas do pais",
    },
    "satana do mundau": {
        "pais": "brasil",
        "populacao": 12000,
        "fato": "cidade que fica as margens do rio mundau",
    },
}

for cidade, informacoes in cidades.items():
    print(cidade, "->", informacoes)
