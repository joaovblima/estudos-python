mel = {
    "tipo": "cachorro",
    "nome_dono": "joao",
}

fred = {
    "tipo": "cachorro",
    "nome_dono": "cicera"
}

louro = {
    "tipo": "papagaio",
    "nome_dono": "maria vitoria",
}

chutrus = {
    "tipo": "gato",
    "nome_dono": "luciana",
}

pets = [mel, fred, louro, chutrus]

for pet in pets:
    print(pet, ", tipo ->", pet["tipo"], "nome do dono ->", pet["nome_dono"])
