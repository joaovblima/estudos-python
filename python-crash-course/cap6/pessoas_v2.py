
joao = {
    "nome": "joao",
    "sobrenome": "lima",
    "idade": 29,
    "time_do_coracao": "spfc"
}

ingrid = {
    "nome": "ingrid",
    "sobrenome": "melo",
    "idade": 26,
    "time_do_coracao": "flamengo"
}

pessoas = [joao, ingrid]

for pessoa in pessoas:
    print(pessoa["nome"].title())
    print(pessoa["sobrenome"].title())
    print(pessoa["idade"])
    print(pessoa["time_do_coracao"].title()+"\n")
